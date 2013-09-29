from ml import *
import PyAmfHelper

def VerifyTypeAndRaise(value, _type):
    if type(value) != _type:
        raise TypeError('value type is "%s", "%s" expected' % (type(value), _type))


class AMFHeader:
    def __init__(self, Name, MustUnderstand, Content):
        self._Name = Name
        self._MustUnderstand = MustUnderstand
        self._Content = Content

    @property
    def Name(self):
        return self._Name

    @property
    def MustUnderstand(self):
        return self._MustUnderstand

    @property
    def Content(self):
        return self._Content

class AMFBody:
    def __init__(self, Target = '', Response = '', Content = None):
        self._Target    = Target
        self._Response  = Response
        self._Content   = [] if Content is None else Content

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, value):
        VerifyTypeAndRaise(value, str)
        self._Target = value

    @property
    def Response(self):
        return self._Response

    @Response.setter
    def Response(self, value):
        VerifyTypeAndRaise(value, str)
        self._Response = value

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, value):
        VerifyTypeAndRaise(value, list)
        self._Content = value

class AMFMessage:
    def __init__(self, Version = 0):
        self._Version = Version
        self._Headers = []
        self._Bodies = []

    @property
    def Version(self):
        return self._Version

    @property
    def HeaderCount(self):
        return len(self._Headers)

    @property
    def BodyCount(self):
        return len(self._Bodies)

    def AddHeader(self, header):
        VerifyTypeAndRaise(header, AMFHeader)
        self._Headers.append(header)

    def AddBody(self, body):
        VerifyTypeAndRaise(body, AMFBody)
        self._Bodies.append(body)

class AMFSerializer:
    def __init__(self):
        self.PyAMFSerializer = PyAmfHelper.PyAMFSerializer()

    def WriteMessage(self, message):
        VerifyTypeAndRaise(message, AMFMessage)
        return self.PyAMFSerializer.WriteMessage(Message = message)

class AMFDeserializer:
    def __init__(self):
        self.PyAMFDeserializer = PyAmfHelper.PyAMFDeserializer()

    def ReadMessage(self, data):
        if type(data) == bytearray:
            data = bytes(data)

        VerifyTypeAndRaise(data, bytes)
        tmp = self.PyAMFDeserializer.ReadMessage(ResponseData = data)
        if tmp is None:
            return None

        msg = AMFMessage()
        msg._Version = tmp['Version']

        return msg

def main():
    dser = AMFDeserializer()

    recv = open('E:\\Desktop\\Source\\WG\\texaspoker\\recv.bin', 'rb').read()
    msg = dser.ReadMessage(recv)
    print(msg._Version)

    input()

    return

    body = AMFBody()
    msg = AMFMessage()
    ser = AMFSerializer()

    content = {}

    content["mid"]      = 17326349
    content["langtype"] = 1
    content["sig"]      = "226e04275fc9afc33106b6be20de067a"
    content["unid"]     = 0
    content["time"]     = "1378374429"
    content["sid"]      = 117
    content["param"]    = None
    content["count"]    = 1
    content["mtkey"]    = "a8b59995a48b7a39f31f975da9e97b95"

    body.Target = 'System.loadInit'
    body.Response = '/1'
    body.Content.append(content)

    msg.AddBody(body)

    bin = ser.WriteMessage(msg)

    #index = 0
    #for x in bin:
    #    print('%02X' % x, end = ' ')
    #    index += 1
    #    if index == 16:
    #        print()
    #        index = 0

    input()

if __name__ == '__main__':
    TryInvoke(main)
