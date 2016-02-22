package trace

type Exception struct {
    Message     string
    Traceback   string
    Value       interface{}
}

func (self *Exception) String() string {
    return "(traceback)\n" + self.Traceback + "\n" + self.Message
}

func (self *Exception) Error() string {
    return self.String()
}

/*

    exception types

*/

type BaseException struct {
    Message string
}

type IndexError struct {
    *BaseException
}

type AttributeError struct {
    *BaseException
}

type KeyError struct {
    *BaseException
}

type NotImplementedError struct {
    *BaseException
}

type FileGenericError struct {
    *BaseException
}

type FileNotFoundError struct {
    *BaseException
}

type PermissionError struct {
    *BaseException
}

func NewBaseException(msg string) *BaseException {
    return &BaseException{Message: msg}
}

func NewIndexError(msg string) *IndexError {
    return &IndexError{
        BaseException: NewBaseException(msg),
    }
}

func NewAttributeError(msg string) *AttributeError {
    return &AttributeError{
        BaseException: NewBaseException(msg),
    }
}

func NewKeyError(msg string) *KeyError {
    return &KeyError{
        BaseException: NewBaseException(msg),
    }
}

func NewNotImplementedError(msg string) *NotImplementedError {
    return &NotImplementedError{
        BaseException: NewBaseException(msg),
    }
}

func NewFileGenericError(msg string) *FileGenericError {
    return &FileGenericError{
        BaseException: NewBaseException(msg),
    }
}

func NewFileNotFoundError(msg string) *FileNotFoundError {
    return &FileNotFoundError{
        BaseException: NewBaseException(msg),
    }
}

func NewPermissionError(msg string) *PermissionError {
    return &PermissionError{
        BaseException: NewBaseException(msg),
    }
}


func (self *BaseException) String() string {
    return self.Message
}

func (self *BaseException) Error() string {
    return self.String()
}