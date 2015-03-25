from Libs.Misc.SysLib import *
import asyncio
import poplib
import http.cookies

class ASYNC_POP3(POP3):
    def __init__(self):
        pass

    def _create_socket(self, timeout):
        return socket.create_connection((self.host, self.port), timeout)

    def _putline(self, line):
        if self._debugging > 1: print('*put*', repr(line))
        self.sock.sendall(line + CRLF)


if poplib.HAVE_SSL:
    class ASYNC_POP3_SSL(POP3_SSL):
        def __init__(self):
            pass
