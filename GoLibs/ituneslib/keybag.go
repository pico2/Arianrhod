package ituneslib

type KeybagSession struct {
    session         uintptr
}

func NewKeybagSession() *KeybagSession {
    session := &KeybagSession{

    }

    return session
}
