from Libs.Misc.SysLib import *
import threading
import requests
import copy

ASYNC_DEFAULT_TIMEOUT = 30

class _HTTPSWithoutCertVerifyAdapter(requests.adapters.HTTPAdapter):
    def send(self, *args, **kwargs):
        kwargs['verify'] = False
        return super().send(*args, **kwargs)

class AsyncHttpRequest(object):
    class _RequestParam(dict2):
        def __init__(self):
            self.Method             = None
            self.Url                = None
            self.CompletionCallback = None
            self.CallbackParameter  = None
            self.QueryStringParams  = None
            self.SendData           = None
            self.Headers            = None
            self.Timeout            = None
            self.AllowRedirects     = True
            self.BytesEncoding      = None
            self.kwargs             = {}

    def __init__(self):
        self.session = requests.sessions.Session()
        self.DefaultHeaders = {
            'User-agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.8 Safari/537.36',
            #'Connection' : 'Keep-Alive',
        }

        self.session.headers = self.DefaultHeaders

        self.Proxies = {
            #'http' : 'http://127.0.0.1:6789',
            #'https' : 'https://127.0.0.1:6789',
        }

    def SetProxy(self, Proxies):
        self.Proxies = Proxies
        if Proxies:
            self.session.mount('https://', _HTTPSWithoutCertVerifyAdapter())
        else:
            self.session.mount('https://', requests.adapters.HTTPAdapter())

    def Close(self):
        self.session.close()

    def Request(
            self,
            Method,
            Url,
            CompletionCallback  = None,
            CallbackParameter   = None,
            QueryStringParams   = None,
            SendData            = None,
            Headers             = None,
            Timeout             = None,
            AllowRedirects      = True,
            Encoding            = None,
            **kwargs
        ):

        param = self._RequestParam()

        param.Url                   = Url
        param.Method                = Method
        param.CompletionCallback    = CompletionCallback
        param.CallbackParameter     = CallbackParameter
        param.QueryStringParams     = QueryStringParams
        param.SendData              = SendData
        param.Headers               = Headers
        param.Timeout               = Timeout
        param.AllowRedirects        = AllowRedirects
        param.BytesEncoding         = Encoding
        param.kwargs                = kwargs

        return self.RequestInternal(**param)

    def RequestText(
            self,
            Method,
            Url,
            CompletionCallback  = None,
            CallbackParameter   = None,
            QueryStringParams   = None,
            SendData            = None,
            Headers             = None,
            Timeout             = None,
            AllowRedirects      = True,
            Encoding            = 'UTF8',
            **kwargs
        ):

        param = self._RequestParam()
        param.Url                   = Url
        param.Method                = Method
        param.CompletionCallback    = CompletionCallback
        param.CallbackParameter     = CallbackParameter
        param.QueryStringParams     = QueryStringParams
        param.SendData              = SendData
        param.Headers               = Headers
        param.Timeout               = Timeout
        param.AllowRedirects        = AllowRedirects
        param.BytesEncoding         = Encoding
        param.kwargs                = kwargs

        return self.RequestInternal(**param)

    def RequestInternal(self, **param):
        param = dict2(param, deep_convert = False)

        def RequestWorker(param):
            if 'proxies' not in param.kwargs:
                param.kwargs['proxies'] = self.Proxies

            response = self.session.request(
                        param.Method,
                        param.Url,
                        params          = param.QueryStringParams,
                        data            = param.SendData,
                        headers         = param.Headers or self.DefaultHeaders,
                        timeout         = param.Timeout,
                        allow_redirects = param.AllowRedirects,
                        **param.kwargs
                    )
            return response

        def DecodeContent(response, encoding):
            return response.content if encoding is None else response.content.decode(encoding)

        def BuildReturnResponse(response, encoding):
            ret = dict2()
            ret['response'] = response

            if response is not None:
                ret['request'] = response.request
                ret['Result'] = DecodeContent(response, encoding)

            return ret

        def RequestThread(RequestParam):
            try:
                response = RequestWorker(RequestParam)
                param = BuildReturnResponse(response, RequestParam.BytesEncoding)
            except Exception as e:
                param = BuildReturnResponse(None, RequestParam.BytesEncoding)
                param['Exception'] = e

            param['Parameter']  = RequestParam.CallbackParameter

            return RequestParam.CompletionCallback(param)

        if param.CompletionCallback is None:
            return BuildReturnResponse(RequestWorker(param), param.BytesEncoding)

        else:

            thread = threading.Thread(target = RequestThread, kwargs = {'RequestParam' : param})
            thread.daemon = True
            thread.start()

            return thread
