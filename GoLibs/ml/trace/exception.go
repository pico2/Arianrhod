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
