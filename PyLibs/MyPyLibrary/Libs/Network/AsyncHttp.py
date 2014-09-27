from Libs.Misc.SysLib import *
import aiohttp
import asyncio
import http.cookies

class AsyncHttp(object):
    class Response(object):
        def __init__(self, response, content):
            self.response = response
            self.content = content

        def __repr__(self):
            return self.response.__repr__()

        def __str__(self):
            return self.response.__str__()

    def __init__(self, *, loop = None, cookie_class = http.cookies.BaseCookie):
        self.loop = loop or asyncio.get_event_loop()
        self.TCPConnector = aiohttp.connector.TCPConnector(share_cookies = True, loop = self.loop)
        self.ProxyConnector = aiohttp.connector.ProxyConnector('http://localhost:80', share_cookies = True, loop = self.loop)

        self.TCPConnector.cookies = cookie_class()
        self.ProxyConnector.cookies = cookie_class()

        self.connector = self.TCPConnector

    @property
    def cookies(self):
        return self.connector.cookies

    def SetCookies(self, cookies):
        self.connector.update_cookies(cookies)

    def SetProxy(self, host, port):
        self.connector = self.ProxyConnector
        self.ProxyConnector._proxy = 'http://%s:%d' % (host, port)
        self.SetCookies(self.TCPConnector.cookies)

    def ClearProxy(self):
        self.connector = self.TCPConnector
        self.SetCookies(self.ProxyConnector.cookies)

    @asyncio.coroutine
    def request(self, method, url, **kwargs):
        kwargs['connector'] = self.connector
        response = yield from aiohttp.request(method, url, **kwargs)
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
