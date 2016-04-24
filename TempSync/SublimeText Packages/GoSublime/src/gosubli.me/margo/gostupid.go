package main

import (
    "os"
    "strings"
    "path/filepath"
)

func normalizeSeparators(path string) string {
    return strings.Replace(strings.Replace(path, "\\", "/", -1), "/", string(filepath.Separator), -1)
}

func pathExists(path string) bool {
    _, err := os.Stat(path)
    return err == nil
}

func findBestPath(gopath []string, dir string) (found string) {
    maxlen := 0
    dir = normalizeSeparators(dir)
    srcPath := "src" + string(filepath.Separator)

    for _, root := range gopath {
        root = normalizeSeparators(root)

        if len(root) > maxlen && strings.HasPrefix(dir, root) {
            maxlen = len(root)
            found = root
            switch (found[len(found) - 1]) {
                case '\\':
                case '/':
                    break

                default:
                    found += string(filepath.Separator)
            }

            if dir[len(found):len(found) + 4] == srcPath {
                found += srcPath
            }
        }
    }
    return
}

func findVendor(gopath, path, pkg string) string {
    gopath = filepath.Join(gopath, ".")
    vendor := filepath.Join("vendor", pkg)
    longest := filepath.Join(path, ".")

    for len(longest) >= len(gopath) {
        v := filepath.Join(longest, vendor)
        if pathExists(v) {
            return v
        }

        longest = filepath.Dir(longest)
    }

    return ""
}

func vendorArchiveOk(roots []string, fn string) bool {
    if len(fn) == 0 {
        return true
    }

    for _, root := range roots {
        if pathExists(filepath.Join(root, fn)) {
            return true
        }
    }
    return false
}
