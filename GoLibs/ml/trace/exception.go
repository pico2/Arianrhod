package trace

type Exception struct {
    Message string
    Value   interface{}
}

func (self *Exception) String() string {
    return self.Message
}

func (self *Exception) Error() string {
    return self.Message
}
