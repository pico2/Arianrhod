package eff

type JsonError struct {
    msg string
}

func (self *JsonError) Error() string {
    return self.msg
}

func (self *JsonError) String() string {
    return self.msg
}
