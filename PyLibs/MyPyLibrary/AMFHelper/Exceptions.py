class UnexpectedAMFEncodingError(Exception):
    def __init__(self, Encoding):
        super().__init__('unexpected amf Encoding: %s' % Encoding)

class UnexpectedAMFTypeCodeError(Exception):
    def __init__(self, TypeCode):
        super().__init__('unexpected amf TypeCode: %s' % TypeCode)

class UnexpectedPyTypeError(Exception):
    def __init__(self, Type):
        super().__init__('unexpected python Type: %s' % Type)
