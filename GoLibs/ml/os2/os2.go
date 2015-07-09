package os2

import (
    "path/filepath"
)

func Executable() string {
    return getExecutable()
}

func ExecutableName() string {
    name := filepath.Base(Executable())
    return name[:len(name) - len(filepath.Ext(name))]
}

func ExecutablePath() string {
    return filepath.Dir(Executable())
}
