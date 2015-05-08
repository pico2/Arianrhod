from Libs.Misc.SysLib import *
import poplib
import asyncio
import http.cookies
import socket
import re
import ssl

error_proto = poplib.error_proto

__all__ = ['ASYNC_POP3', 'error_proto']


POP3_PORT     = poplib.POP3_PORT
POP3_SSL_PORT = poplib.POP3_SSL_PORT
CR            = poplib.CR
LF            = poplib.LF
CRLF          = poplib.CRLF
_MAXLINE      = poplib._MAXLINE


class ASYNC_POP3(asyncio.Protocol):

    """This class supports both the minimal and optional command sets.
    Arguments can be strings or integers (where appropriate)
    (e.g.: retr(1) and retr('1') both work equally well.

    Minimal Command Set:
            USER name               user(name)
            PASS string             pass_(string)
            STAT                    stat()
            LIST [msg]              list(msg = None)
            RETR msg                retr(msg)
            DELE msg                dele(msg)
            NOOP                    noop()
            RSET                    rset()
            QUIT                    quit()

    Optional Commands (some servers support these):
            RPOP name               rpop(name)
            APOP name digest        apop(name, digest)
            TOP msg n               top(msg, n)
            UIDL [msg]              uidl(msg = None)
            CAPA                    capa()
            STLS                    stls()

    Raises one exception: 'error_proto'.

    Instantiate with:
            POP3(hostname, port=110)

    NB:     the POP protocol locks the mailbox from user
            authorization until QUIT, so be sure to get in, suck
            the messages, and quit, each time you access the
            mailbox.

            POP is a line-based protocol, which means large mail
            messages consume lots of python cycles reading them
            line-by-line.

            If it's available on your mail server, use IMAP4
            instead, it doesn't suffer from the two problems
            above.
    """

    encoding = 'UTF-8'

    def __init__(self, host, port = POP3_PORT, timeout = socket._GLOBAL_DEFAULT_TIMEOUT, loop = None):
        super().__init__()

        self.host = host
        self.port = port
        self.timeout = timeout
        self._debugging = 0

        self.loop = loop or asyncio.get_event_loop()

        self.file = None
        self.buffer = bytearray()
        self.transport = None

    def __del__(self):
        self.close()

    @asyncio.coroutine
    def init(self):
        yield from self.create_connection()
        self.welcome = yield from self._getresp()

    @asyncio.coroutine
    def create_connection(self):
        yield from self.loop.create_connection(lambda : self, self.host, self.port)

    ##################################################
    # asyncio.Protocol interface
    ##################################################

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.buffer.extend(data)

    def eof_received(self):
        pass

    def connection_lost(self, exc):
        pass

    ##################################################
    # asyncio.Protocol interface end
    ##################################################

    # Internal: send one command to the server (through _putline())

    @asyncio.coroutine
    def _putline(self, line):
        if self._debugging > 1:
            print('*put*', repr(line))

        self.transport.write(line + CRLF)

    # Internal: send one command to the server (through _putline())

    @asyncio.coroutine
    def _putcmd(self, line):
        if self._debugging:
            print('*cmd*', repr(line))

        line = bytes(line, self.encoding)
        return (yield from self._putline(line))

    # Internal: return one line from the server, stripping CRLF.
    # This is where all the CPU time of this module is consumed.
    # Raise error_proto('-ERR EOF') if the connection is closed.

    @asyncio.coroutine
    def _getline(self):
        index = self.buffer.find(b'\n')

        while index == -1:
            yield from asyncio.sleep(0.1)
            index = self.buffer.find(b'\n')

        line = self.buffer[:index + 1]
        self.buffer[:index + 1] = b''

        if len(line) > _MAXLINE:
            raise error_proto('line too long')

        if self._debugging > 1:
            print('*get*', repr(line))

        if not line:
            raise error_proto('-ERR EOF')

        octets = len(line)
        # server can send any combination of CR & LF
        # however, 'readline()' returns lines ending in LF
        # so only possibilities are ...LF, ...CRLF, CR...LF
        if line[-2:] == CRLF:
            return line[:-2], octets
        if line[0] == CR:
            return line[1:-1], octets
        return line[:-1], octets


    # Internal: get a response from the server.
    # Raise 'error_proto' if the response doesn't start with '+'.

    @asyncio.coroutine
    def _getresp(self):
        resp, o = yield from self._getline()

        if self._debugging > 1:
            print('*resp*', repr(resp))

        if not resp.startswith(b'+'):
            raise error_proto(resp)

        return resp


    # Internal: get a response plus following text from the server.

    @asyncio.coroutine
    def _getlongresp(self):
        resp = yield from self._getresp()
        list = []; octets = 0
        line, o = yield from self._getline()
        while line != b'.':
            if line.startswith(b'..'):
                o = o-1
                line = line[1:]
            octets = octets + o
            list.append(line)
            line, o = yield from self._getline()
        return resp, list, octets


    # Internal: send a command and get the response

    @asyncio.coroutine
    def _shortcmd(self, line):
        yield from self._putcmd(line)
        return (yield from self._getresp())


    # Internal: send a command and get the response plus following text

    @asyncio.coroutine
    def _longcmd(self, line):
        yield from self._putcmd(line)
        return (yield from self._getlongresp())


    # These can be useful:

    def getwelcome(self):
        return self.welcome


    def set_debuglevel(self, level):
        self._debugging = level


    # Here are all the POP commands:

    @asyncio.coroutine
    def user(self, user):
        """Send user name, return response

        (should indicate password required).
        """
        return (yield from self._shortcmd('USER %s' % user))


    @asyncio.coroutine
    def pass_(self, pswd):
        """Send password, return response

        (response includes message count, mailbox size).

        NB: mailbox is locked by server from here to 'quit()'
        """
        return (yield from self._shortcmd('PASS %s' % pswd))


    @asyncio.coroutine
    def stat(self):
        """Get mailbox status.

        Result is tuple of 2 ints (message count, mailbox size)
        """
        retval = yield from self._shortcmd('STAT')
        rets = retval.split()
        if self._debugging: print('*stat*', repr(rets))
        numMessages = int(rets[1])
        sizeMessages = int(rets[2])
        return (numMessages, sizeMessages)


    @asyncio.coroutine
    def list(self, which=None):
        """Request listing, return result.

        Result without a message number argument is in form
        ['response', ['mesg_num octets', ...], octets].

        Result when a message number argument is given is a
        single response: the "scan listing" for that message.
        """
        if which is not None:
            return (yield from self._shortcmd('LIST %s' % which))
        return (yield from self._longcmd('LIST'))


    @asyncio.coroutine
    def retr(self, which):
        """Retrieve whole message number 'which'.

        Result is in form ['response', ['line', ...], octets].
        """
        return (yield from self._longcmd('RETR %s' % which))


    @asyncio.coroutine
    def dele(self, which):
        """Delete message number 'which'.

        Result is 'response'.
        """
        return (yield from self._shortcmd('DELE %s' % which))


    @asyncio.coroutine
    def noop(self):
        """Does nothing.

        One supposes the response indicates the server is alive.
        """
        return (yield from self._shortcmd('NOOP'))


    @asyncio.coroutine
    def rset(self):
        """Unmark all messages marked for deletion."""
        return (yield from self._shortcmd('RSET'))


    @asyncio.coroutine
    def quit(self):
        """Signoff: commit changes on server, unlock mailbox, close connection."""
        resp = yield from self._shortcmd('QUIT')
        self.close()
        return resp

    def close(self):
        self.transport and self.transport.close()

    # __del__ = quit


    # optional commands:

    @asyncio.coroutine
    def rpop(self, user):
        """Not sure what this does."""
        return (yield from self._shortcmd('RPOP %s' % user))


    timestamp = re.compile(br'\+OK.*(<[^>]+>)')

    @asyncio.coroutine
    def apop(self, user, password):
        """Authorisation

        - only possible if server has supplied a timestamp in initial greeting.

        Args:
                user     - mailbox user;
                password - mailbox password.

        NB: mailbox is locked by server from here to 'quit()'
        """
        secret = bytes(password, self.encoding)
        m = self.timestamp.match(self.welcome)
        if not m:
            raise error_proto('-ERR APOP not supported by server')
        import hashlib
        digest = m.group(1)+secret
        digest = hashlib.md5(digest).hexdigest()
        return (yield from self._shortcmd('APOP %s %s' % (user, digest)))


    @asyncio.coroutine
    def top(self, which, howmuch):
        """Retrieve message header of message number 'which'
        and first 'howmuch' lines of message body.

        Result is in form ['response', ['line', ...], octets].
        """
        return (yield from self._longcmd('TOP %s %s' % (which, howmuch)))


    @asyncio.coroutine
    def uidl(self, which=None):
        """Return message digest (unique id) list.

        If 'which', result contains unique id for that message
        in the form 'response mesgnum uid', otherwise result is
        the list ['response', ['mesgnum uid', ...], octets]
        """
        if which is not None:
            return (yield from self._shortcmd('UIDL %s' % which))
        return (yield from self._longcmd('UIDL'))


    @asyncio.coroutine
    def capa(self):
        """Return server capabilities (RFC 2449) as a dictionary
        >>> c=poplib.POP3('localhost')
        >>> c.capa()
        {'IMPLEMENTATION': ['Cyrus', 'POP3', 'server', 'v2.2.12'],
         'TOP': [], 'LOGIN-DELAY': ['0'], 'AUTH-RESP-CODE': [],
         'EXPIRE': ['NEVER'], 'USER': [], 'STLS': [], 'PIPELINING': [],
         'UIDL': [], 'RESP-CODES': []}
        >>>

        Really, according to RFC 2449, the cyrus folks should avoid
        having the implementation split into multiple arguments...
        """
        def _parsecap(line):
            lst = line.decode('ascii').split()
            return lst[0], lst[1:]

        caps = {}
        try:
            resp = yield from self._longcmd('CAPA')
            rawcaps = resp[1]
            for capline in rawcaps:
                capnm, capargs = _parsecap(capline)
                caps[capnm] = capargs
        except error_proto as _err:
            raise error_proto('-ERR CAPA not supported by server')
        return caps


    @asyncio.coroutine
    def stls(self, context=None):
        """Start a TLS session on the active connection as specified in RFC 2595.

                context - a ssl.SSLContext
        """
        if not HAVE_SSL:
            raise error_proto('-ERR TLS support missing')

        if self._tls_established:
            raise error_proto('-ERR TLS session already established')

        caps = self.capa()

        if not 'STLS' in caps:
            raise error_proto('-ERR STLS not supported by server')

        if context is None:
            context = ssl._create_stdlib_context()

        resp = yield from self._shortcmd('STLS')
        self.sock = context.wrap_socket(self.sock, server_hostname = self.host)
        self._tls_established = True
        return resp

if poplib.HAVE_SSL:

    class ASYNC_POP3_SSL(ASYNC_POP3):
        """POP3 client class over SSL connection

        Instantiate with: POP3_SSL(hostname, port=995, keyfile=None, certfile=None,
                                   context=None)

               hostname - the hostname of the pop3 over ssl server
               port - port number

        See the methods of the parent class POP3 for more documentation.
        """

        def __init__(
                self,
                host,
                port    = POP3_SSL_PORT,
                timeout = socket._GLOBAL_DEFAULT_TIMEOUT,
                loop    = None
            ):

            super().__init__(host, port, timeout, loop)

        @asyncio.coroutine
        def create_connection(self):
            yield from self.loop.create_connection(lambda : self, self.host, self.port, ssl = ssl._create_stdlib_context())

        def stls(self, *args, **kwargs):
            """The method unconditionally raises an exception since the
            STLS command doesn't make any sense on an already established
            SSL/TLS session.
            """
            raise error_proto('-ERR TLS session already established')

    __all__.append('ASYNC_POP3_SSL')
