from .AMFTypes import *
import datetime

class AMFReader(FileStream):
    def __init__(self, Stream):
        self.Open(Stream)
        self.Endian = FileStream.BIG_ENDIAN

        self.AMF0Readers = \
        {
           AMF0TypeCode.Number              : self.AMF0ReadNumber,            # 0
           AMF0TypeCode.Boolean             : self.AMF0ReadBoolean,           # 1
           AMF0TypeCode.String              : self.AMF0ReadString,            # 2
           AMF0TypeCode.ASObject            : self.AMF0ReadASObject,          # 3
           AMF0TypeCode.Null                : self.AMF0ReadNull,              # 5
           AMF0TypeCode.Undefined           : self.AMF0ReadUndefined,         # 6
           AMF0TypeCode.Reference           : self.AMF0ReadReference,         # 7
           AMF0TypeCode.AssociativeArray    : self.AMF0ReadAssociativeArray,  # 8
           AMF0TypeCode.Array               : self.AMF0ReadArray,             # 10
           AMF0TypeCode.DateTime            : self.AMF0ReadDateTime,          # 11
           AMF0TypeCode.LongString          : self.AMF0ReadLongString,        # 12
           AMF0TypeCode.Xml                 : self.AMF0ReadXml,               # 15
           AMF0TypeCode.CustomClass         : self.AMF0ReadObject,            # 16
           AMF0TypeCode.AMF3Tag             : self.AMF0ReadAMF3Tag            # 17
        }

        self.AMF3Readers = \
        {
            AMF3TypeCode.Undefined          : self.AMF3ReadNull,           # 0
            AMF3TypeCode.Null               : self.AMF3ReadNull,           # 1
            AMF3TypeCode.BooleanFalse       : self.AMF3ReadBooleanFalse,   # 2
            AMF3TypeCode.BooleanTrue        : self.AMF3ReadBooleanTrue,    # 3
            AMF3TypeCode.Integer            : self.AMF3ReadInteger,        # 4
            AMF3TypeCode.Number             : self.AMF3ReadNumber,         # 5
            AMF3TypeCode.String             : self.AMF3ReadString,         # 6
            AMF3TypeCode.Xml2               : self.AMF3ReadXml,            # 7
            AMF3TypeCode.DateTime           : self.AMF3ReadDateTime,       # 8
            AMF3TypeCode.Array              : self.AMF3ReadArray,          # 9
            AMF3TypeCode.Object             : self.AMF3ReadObject,         # 10
            AMF3TypeCode.Xml                : self.AMF3ReadXml,            # 11
            AMF3TypeCode.ByteArray          : self.AMF3ReadByteArray,      # 12
        }

        self.AMFReaderTable = \
        {
            AMFVersion.AMF0 : self.AMF0Readers,
            AMFVersion.AMF3 : self.AMF3Readers,
        }

        self.Reset()

    def Reset(self):
        self.ObjectReferences = list()
        self.StringReferences = list()
        self.ClassDefinitions = list()

    def AddReferenceObject(self, Object):
        self.ObjectReferences.append(Object)

    def ReferenceObject(self, Handle):
        return self.ObjectReferences[Handle]

    def ReadUTF8(self, Length):
        return (Length == 0) and '' or self.Read(Length).decode('UTF8')

    def ReadData(self, Encoding, TypeCode = None):
        Readers = self.AMFReaderTable.get(Encoding)
        if Readers is None:
            raise UnexpectedAMFEncodingError(Encoding)

        if TypeCode is None:
            TypeCode = self.ReadByte()

        Reader = Readers.get(TypeCode)
        if Reader is None:
            raise UnexpectedAMFTypeCodeError(TypeCode)

        return Reader()

    def ReadAMF0Data(self, TypeCode = None):
        return self.ReadData(AMFVersion.AMF0, TypeCode)

    def ReadAMF3Data(self, TypeCode = None):
        return self.ReadData(AMFVersion.AMF3, TypeCode)

    ##################################################
    # AMF0 type readers
    ##################################################
    def AMF0ReadNumber(self):
        return self.ReadDouble()

    def AMF0ReadBoolean(self):
        return self.ReadBoolean()

    def AMF0ReadString(self):
        return self.ReadUTF8(self.ReadUShort())

    def AMF0ReadDictionary(self, Object):
        while True:
            Key = self.AMF0ReadString()
            TypeCode = self.ReadByte()
            if TypeCode == AMF0TypeCode.EndOfObject:
                break

            Object[Key] = self.ReadAMF0Data(TypeCode)

        self.AddReferenceObject(Object)
        return Object

    def AMF0ReadASObject(self):
        return self.AMF0ReadDictionary(ASObject())

    def AMF0ReadNull(self):
        return None

    def AMF0ReadUndefined(self):
        return AMFUndefined

    def AMF0ReadReference(self):
        return self.ReferenceObject(self.ReadUShort())

    def AMF0ReadAssociativeArray(self):
        Length = self.ReadLong()
        Object = self.AMF0ReadDictionary(AssociativeArray())
        assert(len(Object) == Length)
        return Object

    def AMF0ReadArray(self):
        NumberOfElement = self.ReadLong()
        Array = [self.ReadAMF0Data() for _ in range(NumberOfElement)]
        self.AddReferenceObject(Array)
        return Array

    def AMF0ReadDateTime(self):
        MilliSeconds = self.ReadDouble()
        Minutes = self.ReadUShort()

        # Note for the latter than values greater than 720 (12 hours) are
        # represented as 2^16 - the value.
        # Thus GMT+1 is 60 while GMT-5 is 65236

        if Minutes > 720:
            Minutes = 65536 - Minutes

        Minutes = 0

        return AMFTimeStamp(MilliSeconds / 1000 + Minutes * 60)

    def AMF0ReadLongString(self):
        return self.ReadUTF8(self.ReadLong())

    def AMF0ReadXml(self):
        return ET.fromstring(self.AMF0ReadLongString())

    def AMF0ReadObject(self):
        TypeIdentifier = self.AMF0ReadString()
        Object = self.AMF0ReadASObject()
        Object.TypeName = TypeIdentifier
        return Object

    def AMF0ReadAMF3Tag(self):
        return self.ReadAMF3Data()

    ##################################################
    # amf3 type readers
    ##################################################
    def AMF3ReadNull(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadBooleanFalse(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadBooleanTrue(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadInteger(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadNumber(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadString(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadXml(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadDateTime(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadArray(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadObject(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)

    def AMF3ReadByteArray(self):
        raise NotImplementedError('not implemented type at offset %08X' % self.Position)
