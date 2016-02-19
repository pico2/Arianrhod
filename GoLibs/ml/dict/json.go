package dict

type JsonDict map[string]interface{};
type JsonArray []interface{};

func (self JsonDict) Map(key string) JsonDict {
    i := self[key]
    if i == nil {
        return nil
    }

    return i.(map[string]interface{})
}

func (self JsonDict) Array(key string) JsonArray {
    i := self[key]
    if i == nil {
        return nil
    }

    return i.([]interface{})
}

func (self JsonArray) Map(index int) JsonDict {
    v := self[index]
    if v == nil {
        return nil
    }

    return v.(map[string]interface{})
}

func (self JsonArray) Array(index int) JsonArray {
    v := self[index]
    if v == nil {
        return nil
    }

    return v.([]interface{})
}
