from ml import *
import datetime
from .Exceptions import *

def VerifyTypeAndRaise(value, _type):
    if type(value) != _type:
        raise TypeError('value type is "%s", "%s" expected' % (type(value), _type))

class AMFVersion:
    AMF0 = 0
    AMF3 = 3
    MAX = 4

class AMF0TypeCode:
    Number              = 0
    Boolean             = 1
    String              = 2
    ASObject            = 3
    Null                = 5
    Undefined           = 6
    Reference           = 7
    AssociativeArray    = 8
    EndOfObject         = 9
    Array               = 10
    DateTime            = 11
    LongString          = 12
    Xml                 = 15
    CustomClass         = 16
    AMF3Tag             = 17

    Max                 = 18

class AMF3TypeCode:
    Undefined       = 0
    Null            = 1
    BooleanFalse    = 2
    BooleanTrue     = 3
    Integer         = 4
    Number          = 5
    String          = 6
    DateTime        = 8
    Array           = 9
    Object          = 10
    Xml             = 11
    Xml2            = 7
    ByteArray       = 12

    Max             = 13

AMF0TypeCodeString = {}
AMF3TypeCodeString = {}

for x in dir(AMF0TypeCode):
    if not x.startswith('__'):
        AMF0TypeCodeString[getattr(AMF0TypeCode, x)] = x

for x in dir(AMF3TypeCode):
    if not x.startswith('__'):
        AMF3TypeCodeString[getattr(AMF3TypeCode, x)] = x


class AMFHeader:
    #CredentialsHeader       = "Credentials"
    #DebugHeader             = "amf_server_debug"
    #ServiceBrowserHeader    = "DescribeService"
    #ClearedCredentials      = "ClearedCredentials"
    #CredentialsIdHeader     = "CredentialsId"
    #RequestPersistentHeader = "RequestPersistentHeader"

    def __init__(self, Name, MustUnderstand, Content):
        self._Name              = Name
        self._MustUnderstand    = MustUnderstand
        self._Content           = Content

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
    #Recordset       = "rs://"
    #OnResult        = "/onResult"
    #OnStatus        = "/onStatus"
    #OnDebugEvents   = "/onDebugEvents"

    def __init__(self, Target, Response, Content = None):
        self._Target     = Target
        self._Response   = Response
        self._Content    = Content

    @property
    def Target(self):
        return self._Target

    @property
    def Response(self):
        return self._Response

    @property
    def Content(self):
        return self._Content

    @property
    def IsEmptyTarget(self):
        return self._Target is None or self._Target == '' or self._Target == 'null'

class AMFMessage:
    def __init__(self, Version = AMFVersion.AMF0):
        self._Version = Version
        self._Headers = list()
        self._Bodies = list()

    @property
    def Encoding(self):
        if self._Version == 0 or self._Version == 1:
            return AMFVersion.AMF0

        if self._Version == 3:
            return AMFVersion.AMF3

        raise UnexpectedAMFEncodingError(self._Version)

    @property
    def Version(self):
        return self._Version

    @property
    def HeaderCount(self):
        return len(self._Headers)

    @property
    def BodyCount(self):
        return len(self._Bodies)

    @property
    def Headers(self):
        return self._Headers.copy()

    @property
    def Bodies(self):
        return self._Bodies.copy()

    def AddHeader(self, header):
        VerifyTypeAndRaise(header, AMFHeader)
        self._Headers.append(header)

    def AddBody(self, body):
        VerifyTypeAndRaise(body, AMFBody)
        self._Bodies.append(body)

    def GetHeader(self, HeaderName):
        for header in self._Headers:
            if header.Name == HeaderName:
                return header

        return None

    def RemoveHeader(self, HeaderName):
        for index, header in enumerate(self._Headers):
            if header.Name == HeaderName:
                self._Headers.pop(index)
                return

class AMFUndefinedType(object):
    pass

AMFUndefined = AMFUndefinedType()

class ASObject(OrderedDictEx):
    __slots__ = ('TypeName')

class AssociativeArray(OrderedDictEx):
    pass

class AMFTimeStamp:
    def __init__(self, TimeStamp):
        self._TimeStamp = TimeStamp
        self._Date = datetime.datetime.fromtimestamp(TimeStamp)

    def __str__(self):
        return str(self._Date)

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @property
    def Date(self):
        return self._Date

if __name__ == '__main__':
    from ml import *

    def main():
        import time
        print(AMFTimeStamp(time.time()))
        PauseConsole()

    TryInvoke(main)
