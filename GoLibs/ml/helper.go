package ml

func If(cond bool, True interface{}, False interface{}) interface{} {
    if cond {
        return True
    }

    return False
}
