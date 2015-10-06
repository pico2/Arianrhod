package eff

import (
    . "ml/strings"
)

type Effect interface {
    Name()      String
    Texture()   []String
    Children()  []String
}

type EffectBase struct {
    Effect

    name        String
    texture     []String
    children    []String
}

func newEffectBase() *EffectBase {
    return &EffectBase{}
}

func (self *EffectBase) Name() String {
    return self.name
}

func (self *EffectBase) Texture() []String {
    return self.name
}

func (self *EffectBase) Children() []String {
    return self.name
}
