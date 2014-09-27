from .AMFReader import *

class AMFDeserializer(AMFReader):
    def __init__(self, Stream):
        super().__init__(Stream)

    def ReadMessage(self):
        Version = self.ReadUShort()
        Message = AMFMessage(Version)

        HeaderCount = self.ReadUShort()
        for _ in range(HeaderCount):
            Message.AddHeader(self.ReadHeader(Message.Encoding))

        BodyCount = self.ReadUShort()
        for _ in range(BodyCount):
            Message.AddBody(self.ReadBody(Message.Encoding))

        return Message

    def ReadHeader(self, Encoding):
        self.Reset()

        HeaderName      = self.AMF0ReadString()
        MustUnderstand  = self.ReadBoolean()
        HeaderLength    = self.ReadLong()
        Content         = self.ReadData(Encoding)

        return AMFHeader(HeaderName, MustUnderstand, Content)

    def ReadBody(self, Encoding):
        self.Reset()

        Target      = self.AMF0ReadString()
        Response    = self.AMF0ReadString()
        Length      = self.ReadLong()
        Content     = self.ReadData(Encoding)

        return AMFBody(Target, Response, Content)

if __name__ == '__main__':
    from ml import *

    def main():
        amf = AMFDeserializer(open('Tables.getGameZoneTables.send.bin', 'rb').read())
        msg = amf.ReadMessage()
        info = FormatObject(msg, itergen = iter)
        print(''.join(info))
        PauseConsole()

    TryInvoke(main)
