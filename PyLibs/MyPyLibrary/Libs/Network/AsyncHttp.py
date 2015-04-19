from Libs.Misc.SysLib import *
import aiohttp
import asyncio
import http.cookies

class Request(aiohttp.Request):
    def __init__(self, *args, **kwargs):
        ibp()
        super().__init__(*args, **kwargs)
        self.headers = _CaseInsensitiveDict()

    def _add_default_headers(self):
        aiohttp.HttpMessage._add_default_headers(self)
        # super()._add_default_headers()

    def add_header(self, name, value):
        """Analyze headers. Calculate content length,
        removes hop headers, etc."""
        assert not self.headers_sent, 'headers have been sent already'
        assert isinstance(name, str), 'Header name should be a string, got {!r}'.format(name)
        assert set(name).issubset(aiohttp.protocol.ASCIISET), 'Header name should contain ASCII chars, got {!r}'.format(name)
        assert isinstance(value, str), 'Header {!r} should have string value, got {!r}'.format(name, value)

        name = name.strip()
        value = value.strip()

        name_upper = name.upper()

        if name_upper == 'CONTENT-LENGTH':
            self.length = int(value)

        if name_upper == 'CONNECTION':
            val = value.lower()
            # handle websocket
            if 'upgrade' in val:
                self.upgrade = True
            # connection keep-alive
            elif 'close' in val:
                self.keepalive = False
            elif 'keep-alive' in val and self.version >= aiohttp.protocol.HttpVersion11:
                self.keepalive = True

        elif name_upper == 'UPGRADE':
            if 'websocket' in value.lower():
                self.websocket = True
                self.headers[name] = value

        elif name_upper == 'TRANSFER-ENCODING' and not self.chunked:
            self.chunked = value.lower().strip() == 'chunked'

        elif name_upper not in self.HOP_HEADERS:
            if name_upper == 'USER-AGENT':
                self._has_user_agent = True

            # ignore hop-by-hop headers
            self.headers.add(name, value)

aiohttp.Request = Request

class _CaseInsensitiveDict(CaseInsensitiveDict):
    def add(self, key, value):
        self[key] = value

    def items(self, **kwargs):
        return super().items()

class _ClientRequest(aiohttp.client.ClientRequest):
    def update_cookies(self, cookies):
        """Update request cookies header."""
        if not cookies:
            return

        c = http.cookies.BaseCookie()
        if 'COOKIE' in self.headers:
            c.load(self.headers.get('COOKIE', ''))
            del self.headers['COOKIE']

        if isinstance(cookies, dict):
            cookies = cookies.items()

        for name, value in cookies:
            if isinstance(value, http.cookies.Morsel):
                # use dict method because SimpleCookie class modifies value
                dict.__setitem__(c, name, value)
            else:
                c[name] = value

        # ibp()
        self.headers['Cookie'] = c.output(header='', sep=';', attrs = {}).strip()

    def update_headers(self, headers):
        """Update request headers."""
        self.headers = _CaseInsensitiveDict()

        if headers:
            if isinstance(headers, dict):
                headers = headers.items()
            elif isinstance(headers, MultiDict):
                headers = headers.items()

            for key, value in headers:
                self.headers[key] = value

        # DEFAULT_HEADERS = {
        #     'Accept': '*/*',
        #     'Accept-Encoding': 'gzip, deflate',
        # }

        # for hdr, val in DEFAULT_HEADERS.items():
        #     if hdr not in self.headers:
        #         self.headers[hdr] = val

        # add host
        if 'HOST' not in self.headers:
            self.headers['Host'] = self.netloc

class AsyncHttp(object):
    class Response(object):
        def __init__(self, response, content):
            self.response = response
            self.content = content

        def __repr__(self):
            return self.response.__repr__()

        def __str__(self):
            return self.response.__str__()

        @property
        def status(self):
            return self.response.status

        def plist(self):
            import plistlib
            return plistlib.loads(self.content)

        def json(self, encoding = None):
            return dict2(json.loads(self.decode(encoding)))

        def text(self, encoding = None):
            return self.decode(encoding)

        def decode(self, encoding = None, **kwargs):
            return self.content.decode(self.response._get_encoding(encoding), **kwargs)

    def __init__(self, *, loop = None, timeout = 30, cookie_class = http.cookies.BaseCookie):
        self.loop = loop or asyncio.get_event_loop()
        self.TCPConnector = aiohttp.connector.TCPConnector(verify_ssl = False, share_cookies = True, loop = self.loop)
        self.ProxyConnector = aiohttp.connector.ProxyConnector('http://localhost:80', verify_ssl = False, share_cookies = True, loop = self.loop)

        self.TCPConnector.cookies = cookie_class()
        self.ProxyConnector.cookies = cookie_class()

        self.headers = {}
        self.timeout = timeout

        self.connector = self.TCPConnector

    @property
    def cookies(self):
        return self.connector.cookies

    def SetHeaders(self, headers):
        self.headers = headers

    def SetCookies(self, cookies):
        if not cookies:
            self.connector.cookies.clear()
        else:
            self.connector.update_cookies(cookies)

    def SetProxy(self, host, port, login = None, password = None, encoding = 'latin1'):
        if self.connector is not self.ProxyConnector:
            self.connector = self.ProxyConnector
            self.SetCookies(self.TCPConnector.cookies)

        self.ProxyConnector._proxy = 'http://%s:%d' % (host, port)

        if login is not None and password is not None:
            self.ProxyConnector._proxy_auth = aiohttp.helpers.BasicAuth(login, password, encoding)

    def ClearProxy(self):
        if self.connector is not self.ProxyConnector:
            return

        self.connector = self.TCPConnector
        self.SetCookies(self.ProxyConnector.cookies)

    @asyncio.coroutine
    def request(self, method, url, **kwargs):
        kwargs['connector'] = self.connector
        kwargs['request_class'] = _ClientRequest

        if 'headers' not in kwargs:
            kwargs['headers'] = self.headers
        else:
            hdr = self.headers.copy()
            for k, v in kwargs['headers'].items():
                hdr[k] = v

            kwargs['headers'] = hdr

        try:
            response = yield from asyncio.wait_for(aiohttp.request(method, url, **kwargs), self.timeout)
        except asyncio.TimeoutError:
            raise asyncio.TimeoutError('%s %s timeout: %s' % (method, url, self.timeout))

        content = yield from response.read()

        return self.Response(response, content)

if __name__ == '__main__':
    def main2():
        http = AsyncHttp()

        http.SetProxy('localhost', 6789)

        r = yield from http.request('get', 'http://www.baidu.com')
        print(r)

    def main():
        l = asyncio.get_event_loop()
        l.run_until_complete(main2())

        PauseConsole('done')

    TryInvoke(main)
