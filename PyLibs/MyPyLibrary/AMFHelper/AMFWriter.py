from .AMFTypes import *
import datetime

class AMFWriter(FileStream):
    def __init__(self, Stream):
        self.Open(Stream)
        self.Endian = FileStream.BIG_ENDIAN

        self.AMF0Writers = \
        {
            int                 : self.AMF0WriteNumber,
            float               : self.AMF0WriteNumber,
            bool                : self.AMF0WriteBoolean,
            str                 : self.AMF0WriteString,
            dict                : self.AMF0WriteASObject,
            dict2               : self.AMF0WriteASObject,
            ASObject            : self.AMF0WriteASObject,
            OrderedDict         : self.AMF0WriteASObject,
            OrderedDictEx       : self.AMF0WriteASObject,
            type(None)          : self.AMF0WriteNull,
            AMFUndefinedType    : self.AMF0WriteUndefined,
            AssociativeArray    : self.AMF0WriteASObject,
            list                : self.AMF0WriteArray,
            tuple               : self.AMF0WriteArray,
            AMFTimeStamp        : self.AMF0WriteDateTime,
            ET.Element          : self.AMF0WriteXmlElement,
            ET.ElementTree      : self.AMF0WriteXmlElementTree,
        }

        self.AMF3Writers = {}

        self.AMFWriterTable = \
        {
            AMFVersion.AMF0 : self.AMF0Writers,
            AMFVersion.AMF3 : self.AMF3Writers,
        }

    def Reset(self):
        self.ObjectReferences            = list()
        self.StringReferences            = dict()
        self.ClassDefinitionReferences   = dict()

    def AddReferenceObject(self, Object):
        if self.ReferenceObject(Object) is None:
            if len(self.ObjectReferences) > 0xFFFF:
                raise Exception('too many object referenced')

            self.ObjectReferences.append(Object)

    def ReferenceObject(self, Object):
        try:
            return self.ObjectReferences.index(Object)
        except ValueError:
            return None

    def WriteData(self, Data, Encoding):
        Writers = self.AMFWriterTable.get(Encoding)
        if Writers is None:
            raise UnexpectedAMFEncodingError(Encoding)

        Handle = self.ReferenceObject(Data)
        if Handle is not None:
            return self.AMF0WriteReference(Handle)

        Writer = Writers.get(type(Data))
        if Writer is None:
            raise UnexpectedPyTypeError(type(Data))

        return Writer(Data)

    def WriteAMF0Data(self, Data):
        return self.WriteData(Data, AMFVersion.AMF0)

    def WriteAMF3Data(self, Data):
        return self.WriteData(Data, AMFVersion.AMF3)

    def WriteShortString(self, String):
        if String is None or  len(String) == 0:
            self.WriteUShort(0)
            return

        String = String.encode('UTF8')
        self.WriteUShort(len(String))
        self.Write(String)

    ##################################################
    # amf0 writer
    ##################################################

    def AMF0WriteReference(self, Handle):
        self.WriteByte(AMF0TypeCode.Reference)
        self.WriteUShort(Handle)

    def AMF0WriteEndOfObject(self):
        self.WriteShortString('')
        self.WriteByte(AMF0TypeCode.EndOfObject)

    def AMF0WriteNumber(self, Number):
        self.WriteByte(AMF0TypeCode.Number)
        self.WriteDouble(Number)

    def AMF0WriteBoolean(self, Boolean):
        self.WriteByte(AMF0TypeCode.Boolean)
        self.WriteBoolean(Boolean)

    def AMF0WriteASObject(self, Object):
        self.AddReferenceObject(Object)

        if hasattr(Object, 'TypeName') and Object.TypeName is not None:
            self.WriteByte(AMF0TypeCode.CustomClass)
            self.WriteShortString(Object.TypeName)

        elif isinstance(Object, AssociativeArray):
            self.WriteByte(AMF0TypeCode.AssociativeArray)
            self.WriteLong(len(Object))

        else:
            self.WriteByte(AMF0TypeCode.ASObject)

        for Key, Value in Object.items():
            self.WriteShortString(Key)
            self.WriteAMF0Data(Value)

        self.AMF0WriteEndOfObject()

    def AMF0WriteNull(self, Null):
        assert(Null is None)
        self.WriteByte(AMF0TypeCode.Null)

    def AMF0WriteUndefined(self, Undefined):
        assert(Undefined is AMFUndefined)
        self.WriteByte(AMF0TypeCode.Undefined)

    def AMF0WriteArray(self, Array):
        #self.AddReferenceObject(Array)
        self.WriteByte(AMF0TypeCode.Array)
        self.WriteLong(len(Array))
        for x in Array:
            self.WriteAMF0Data(x)

    def AMF0WriteString(self, Data):
        Data = Data.encode('UTF8')
        if len(Data) <= 0xFFFF:
            self.WriteByte(AMF0TypeCode.String)
            self.WriteUShort(len(Data))
        else:
            self.WriteByte(AMF0TypeCode.LongString)
            self.WriteLong(len(Data))

        self.Write(Data)

    def AMF0WriteDateTime(self, DateTime):
        self.WriteByte(AMF0TypeCode.DateTime)
        self.WriteDouble(DateTime.TimeStamp * 1000)
        self.WriteUShort(0)

    def AMF0WriteXmlElement(self, Data):
        raise NotImplementedError('%08X' % self.Position)

    def AMF0WriteXmlElementTree(self, Data):
        raise NotImplementedError('%08X' % self.Position)

