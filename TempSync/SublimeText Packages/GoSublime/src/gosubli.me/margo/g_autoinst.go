package main

import (
	"go/parser"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

var (
	autoInstCh = make(chan AutoInstOptions, 10)
)

func autoInstall(ao AutoInstOptions) {
	select {
	case autoInstCh <- ao:
	default:
	}
}

type AutoInstOptions struct {
	// if ImportPaths is empty, Src is parsed in order to populate it
	ImportPaths []string
	Src         string
	Dir         string

	// the environment variables as passed by the client - they should not be merged with os.Environ(...)
	// GOPATH is be valid
	Env map[string]string

	// the installsuffix to use for pkg paths
	InstallSuffix string
}

func (a *AutoInstOptions) imports() map[string]string {
	m := map[string]string{}

	if len(a.ImportPaths) == 0 {
		_, af, _ := parseAstFile("a.go", a.Src, parser.ImportsOnly)
		a.ImportPaths = fileImportPaths(af)
	}

	for _, p := range a.ImportPaths {
		m[p] = filepath.FromSlash(p) + ".a"
	}

	return m
}

func (a *AutoInstOptions) install() {
	sfx := ""
	if a.InstallSuffix != "" {
		sfx = a.InstallSuffix
	}
	osArchSfx := osArch + sfx
	if a.Env == nil {
		a.Env = map[string]string{}
	}

	roots := []string{}

	if p := a.Env["GOROOT"]; p != "" {
		roots = append(roots, filepath.Join(p, "pkg", osArchSfx))
	}

	for _, p := range pathList(a.Env["GOPATH"]) {
		roots = append(roots, filepath.Join(p, "pkg", osArchSfx))
	}

	if len(roots) == 0 {
		return
	}

	archiveOk := func(fn string) bool {
		for _, root := range roots {
			_, err := os.Stat(filepath.Join(root, fn))
			if err == nil {
				return true
			}
		}
		return false
	}

	el := envSlice(a.Env)
	installed := []string{}

	normalizeSeparators := func (path string) string {
		return strings.Replace(strings.Replace(path, "\\", "/", -1), "/", string(filepath.Separator), -1)
	}

	findBestPath := func (dir string) (found string) {
		maxlen := 0
		dir = normalizeSeparators(dir)

		for _, root := range pathList(a.Env["GOPATH"]) {
			root = normalizeSeparators(root)

			if strings.HasPrefix(dir, root) && len(root) > maxlen {
				maxlen = len(root)
				found = root
				switch (found[len(found) - 1]) {
					case '\\':
					case '/':

					default:
						found += string(filepath.Separator)
				}
			}
		}
		return
	}

	bestPath := findBestPath(a.Dir)

	for path, fn := range a.imports() {
		if path[0] == '.' && len(bestPath) != 0 {
			// relative package path
			path = filepath.Join(a.Dir, path)
			fn = filepath.Join(a.Dir, fn)
			path = path[len(bestPath):]
			fn = fn[len(bestPath):]
		}

		if !archiveOk(fn) {
			var cmd *exec.Cmd
			if sfx == "" {
				cmd = exec.Command("go", "install", path)
			} else {
				cmd = exec.Command("go", "install", "-installsuffix", sfx, path)
			}
			cmd.Env = el
			cmd.Stderr = ioutil.Discard
			cmd.Stdout = ioutil.Discard
			cmd.Run()

			if archiveOk(fn) {
				installed = append(installed, path)
			}
		}
	}

	if len(installed) > 0 {
		postMessage("auto-installed: %v", strings.Join(installed, ", "))
	}
}

func init() {
	go func() {
		for ao := range autoInstCh {
			ao.install()
		}
	}()
}
