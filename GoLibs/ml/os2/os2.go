package os2

import (
    "path/filepath"
)

func Executable() string {
    return getExecutable()
}

func ExecutablePath() string {
    return filepath.Dir(Executable())
}
