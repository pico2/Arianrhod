package dict

type JsonDict map[string]interface{};
type JsonArray []interface{};

func (self JsonDict) Map(key string) JsonDict {
    return self[key].(map[string]interface{})
}

func (self JsonDict) Array(key string) JsonArray {
    return self[key].([]interface{})
}

func (self JsonArray) Map(index int) JsonDict {
    return self[index].(map[string]interface{})
}

func (self JsonArray) Array(index int) JsonArray {
    return self[index].([]interface{})
}

