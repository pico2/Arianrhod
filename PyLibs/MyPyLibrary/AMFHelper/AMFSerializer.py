from .AMFWriter import *

class AMFSerializer(AMFWriter):
    def __init__(self):
        super().__init__(b'')

    def WriteMessage(self, Message):
        self.Length = 0

        self.WriteUShort(Message.Version)
        self.WriteUShort(Message.HeaderCount)
        for Header in Message.Headers:
            self.WriteHeader(Header, Message.Encoding)

        self.WriteUShort(Message.BodyCount)
        for Body in Message.Bodies:
            self.WriteBody(Body, Message.Encoding)

        with FileStreamPositionHolder(self):
            self.Position = 0
            return self.Read()

    def WriteHeader(self, Header, Encoding):
        self.Reset()

        self.WriteShortString(Header.Name)
        self.WriteBoolean(Header.MustUnderstand)
        self.WriteLong(-1)
        HeaderBegin = self.Position
        self.WriteData(Header.Content, Encoding)
        HeaderEnd = self.Position
        with FileStreamPositionHolder(self):
            self.Position = HeaderBegin - 4
            self.WriteLong(HeaderEnd - HeaderBegin)

    def WriteBody(self, Body, Encoding):
        self.Reset()

        self.WriteShortString(Body.Target or 'null')
        self.WriteShortString(Body.Response or 'null')
        self.WriteLong(-1)
        BodyBegin = self.Position
        self.WriteData(Body.Content, Encoding)
        BodyEnd = self.Position
        with FileStreamPositionHolder(self):
            self.Position = BodyBegin - 4
            self.WriteLong(BodyEnd - BodyBegin)


if __name__ == '__main__':
    from ml import *

    def main():
        from AMFDeserializer import AMFDeserializer

        infile = 'Members.onlineReward.send.bin'

        amf = AMFDeserializer(open(infile, 'rb').read())
        msg = amf.ReadAMFMessage()
        info = FormatObject(msg, itergen = iter)
        print(''.join(info))

        amf = AMFSerializer()
        bin = amf.WriteMessage(msg)
        open('amf.bin', 'wb').write(bin)

        os.system('fc/b amf.bin %s' % infile)
        PauseConsole()

    TryInvoke(main)
