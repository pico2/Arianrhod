package eff

import (
    . "ml/strings"
)

type Effect interface {
    Name()                  String
    Texture()               []String
    Children()              []String
    Serialize()             []byte
    Unserialize([]byte)     Effect
}

type EffectBase struct {
    Effect

    fileName    String
    name        String
    texture     []String
    children    []String
}

func newEffectBase() *EffectBase {
    return &EffectBase{
        texture:    []String{},
        children:   []String{},
    }
}

func (self *EffectBase) FileName() String {
    return self.fileName
}

func (self *EffectBase) Name() String {
    return self.name
}

func (self *EffectBase) Texture() []String {
    return self.texture
}

func (self *EffectBase) Children() []String {
    return self.children
}
