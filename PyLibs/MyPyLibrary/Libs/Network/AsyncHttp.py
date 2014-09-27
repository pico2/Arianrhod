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

        cookies = json.loads(r'{"api":"com.taobao.client.sys.login","v":"v3","ret":["SUCCESS::调用成功"],"data":{"time":"20140914","cookies":["imewweoriw=3%2FwUb%2BTuapqJvNKDVOSfyjAzxEA7lu5KGpzFnthWAxc%3D; Domain=.m.taobao.com; Expires=Sun, 21-Sep-2014 20:25:01 GMT; Path=/","WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuXlDsaEEjGDG6UA7toRAXxaStGgHs9CSEc7uuAt%2B9j5a; Domain=.m.taobao.com; Expires=Mon, 14-Sep-2015 20:25:01 GMT; Path=/","_w_tb_nick=%E5%8D%A1%E5%B8%83%E5%A5%87%E8%AF%BA_520; Domain=.m.taobao.com; Expires=Sun, 21-Sep-2014 20:25:01 GMT; Path=/","ockeqeudmj=nhAAVlQ%3D; Domain=.m.taobao.com; Expires=Sun, 21-Sep-2014 20:25:01 GMT; Path=/","imewweoriw=3%2FwUb%2BTuapqJvNKDVOSfyjAzxEA7lu5KGpzFnthWAxc%3D; Domain=.m.etao.com; Expires=Sun, 21-Sep-2014 20:25:01 GMT; Path=/","WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuXlDsaEEjGDG6UA7toRAXxaStGgHs9CSEc7uuAt%2B9j5a; Domain=.m.etao.com; Expires=Mon, 14-Sep-2015 20:25:01 GMT; Path=/","_w_tb_nick=%E5%8D%A1%E5%B8%83%E5%A5%87%E8%AF%BA_520; Domain=.m.tmall.com; Expires=Sun, 21-Sep-2014 20:25:01 GMT; Path=/","imewweoriw=3%2FwUb%2BTuapqJvNKDVOSfyjAzxEA7lu5KGpzFnthWAxc%3D; Domain=.m.tmall.com; Expires=Sun, 21-Sep-2014 20:25:01 GMT; Path=/","WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuXlDsaEEjGDG6UA7toRAXxaStGgHs9CSEc7uuAt%2B9j5a; Domain=.m.tmall.com; Expires=Mon, 14-Sep-2015 20:25:01 GMT; Path=/","_w_tb_nick=%E5%8D%A1%E5%B8%83%E5%A5%87%E8%AF%BA_520; Domain=.m.etao.com; Expires=Sun, 21-Sep-2014 20:25:01 GMT; Path=/","yryetgfhth=%2B4cXpeDzLTAIW6kFUQRV8YC1UQyCPseunLF0odzw7sCEBb1mMhWh4PZiAGDN4QU3FWzHvu8B54M1tag1dn5vEVmwT5y%2FpNGkz2aOMm9JmHZ95N%2BlJSyDELOuwxO8Yk8%2BMXVxPsEa8yClTwFsgvm%2BS14hExkawbTh5VtTBhBovih83A%3D%3D; Domain=.login.m.taobao.com; Expires=Mon, 14-Sep-2015 20:25:01 GMT; Path=/","yryetgfhth=%2B4cXpeDzLTAIW6kFUQRV8YC1UQyCPseunLF0odzw7sCEBb1mMhWh4PZiAGDN4QU3FWzHvu8B54M1tag1dn5vEVmwT5y%2FpNGkz2aOMm9JmHZ95N%2BlJSyDELOuwxO8Yk8%2BMXVxPsEa8yClTwFsgvm%2BS14hExkawbTh5VtTBhBovih83A%3D%3D; Domain=.login.m.etao.com; Expires=Mon, 14-Sep-2015 20:25:01 GMT; Path=/","yryetgfhth=%2B4cXpeDzLTAIW6kFUQRV8YC1UQyCPseunLF0odzw7sCEBb1mMhWh4PZiAGDN4QU3FWzHvu8B54M1tag1dn5vEVmwT5y%2FpNGkz2aOMm9JmHZ95N%2BlJSyDELOuwxO8Yk8%2BMXVxPsEa8yClTwFsgvm%2BS14hExkawbTh5VtTBhBovih83A%3D%3D; Domain=.login.m.tmall.com; Expires=Mon, 14-Sep-2015 20:25:01 GMT; Path=/","_w_al_f=1; Domain=.m.etao.com; Expires=Sun, 28-Sep-2014 20:25:01 GMT; Path=/","_w_al_f=1; Domain=.m.tmall.com; Expires=Sun, 28-Sep-2014 20:25:01 GMT; Path=/","_w_al_f=1; Domain=.m.taobao.com; Expires=Sun, 28-Sep-2014 20:25:01 GMT; Path=/","uc1=cookie14=UoW282eUCEfa7g%3D%3D&cookie21=UtASsssmeJpuuXUmxw%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D;Domain=.taobao.com;Path=/;","uc3=nk2=3ByDf3BD1glpFXK3&id2=UNJV2EGMPB%2BZ&vt3=F8dATSFQTk%2BpfSjWJcc%3D&lg2=UtASsssmOIJ0bQ%3D%3D;Domain=.taobao.com;Path=/;Expires=Tue, 14-Oct-2014 20:25:01 GMT;HttpOnly","skt=1b3d9eb7a63412ca;Domain=.taobao.com;Path=/;HttpOnly","lgc=%5Cu5361%5Cu5E03%5Cu5947%5Cu8BFA_520;Domain=.taobao.com;Path=/;Expires=Tue, 14-Oct-2014 20:25:01 GMT;","_cc_=UtASsssmfA%3D%3D;Domain=.taobao.com;Path=/;Expires=Mon, 14-Sep-2015 20:25:01 GMT;","t=13258ffe66682f8f5d39a14f7cc765e5;Domain=.taobao.com;Path=/;Expires=Sat, 13-Dec-2014 20:25:01 GMT;","unb=324527313;Domain=.taobao.com;Path=/;HttpOnly","_nk_=%5Cu5361%5Cu5E03%5Cu5947%5Cu8BFA_520;Domain=.taobao.com;Path=/;","_l_g_=Ug%3D%3D;Domain=.taobao.com;Path=/;","cookie1=VAXYJrf7P%2BlsjZZtTq3klyVPT1khX1VvQRe%2BOILl9Vg%3D;Domain=.taobao.com;Path=/;HttpOnly","cookie2=1d1e2bfb01b2422d6cf6ffe414a608e7;Domain=.taobao.com;Path=/;HttpOnly","cookie17=UNJV2EGMPB%2BZ;Domain=.taobao.com;Path=/;HttpOnly","tracknick=%5Cu5361%5Cu5E03%5Cu5947%5Cu8BFA_520;Domain=.taobao.com;Path=/;Expires=Mon, 14-Sep-2015 20:25:01 GMT;","sg=03b;Domain=.taobao.com;Path=/;","cookie2=1d1e2bfb01b2422d6cf6ffe414a608e7;Domain=.taobao.com;Path=/;HttpOnly","_tb_token_=35b7118e1e7f1;Domain=.taobao.com;Path=/;HttpOnly","cookie2=; Domain=.tmall.com; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","cookie2=; Domain=.etao.com; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","cookie2=; Domain=.hitao.com; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","cookie2=; Domain=.yao.95095.com; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/","cookie2=; Domain=.tdd.la; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/"],"userId":"324527313","nick":"卡布奇诺_520","token":"29a84c22802b6d786fc0eec23b862e8de4aff923609afee37591a4495b16612ccfaeabb40a88ac9900592a9e01b6c93dd3685b20a9c86dc0064af5c3adb4b3754ba33560eaed062d7aed7558b421aeaabb2f6407067fd8eb1e13e11a378948e4f46e15b547d7034aae7ed642e31f7a162066d2a0f1f5ff8cf1ef01f043294baa15c6c054417dd8caa920934cdd0228f336e64e8d0fe0499d2d8f5f3d5b937b3068fb49677927537c62ed8f263a482cc6311c95a7d6fcc9f1d0e2be61acd34a38","sid":"1d1e2bfb01b2422d6cf6ffe414a608e7","phone":"18505976161","ecode":"pbIXT","ssoToken":"9Hl53ZFQT5g3TR9+bAeDXCuJ5X5a5Ql+05CElib0drMqw/9A5P4+GxoPtGvcauKMq2v62Y1DJ19/IVL570qcT1Wd8fQiRhCAVr8jMhoRaLvqbxT4J+3VBzXD2bDWOJ1hOCUCVQ927p6bmTAc7zbq1DvFwAQkGXF2XiBua955oXZrn/DbqCi2+zrafb657FpVjfrg1jFRtzPa/g8e+la83uAysY/FCoVmx2hrV9/jekYNe7crHPoq15aXv4xqm3hF","logintime":"1410726301"}}')
        cookies = cookies['data']['cookies']

        cookies2 = dict()
        for item in cookies:
            name, value = item.split('=', maxsplit = 1)
            value = value.split(';', maxsplit = 1)[0]

            if value:
                cookies2[name] = value

        cookies = cookies2

        http.SetCookies(cookies)

        r = yield from http.request('get', 'http://www.baidu.com')
        print(r)

    def main():
        l = asyncio.get_event_loop()
        l.run_until_complete(main2())

        PauseConsole('done')

    TryInvoke(main)
