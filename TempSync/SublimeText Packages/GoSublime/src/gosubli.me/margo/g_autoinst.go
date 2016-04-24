package main

import (
	"go/parser"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"fmt"
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
	alwaysInstall := a.Env["ALWAYS_INSTALL"] == "1"
	goSrc := a.Env["GOROOT"] + "/src/"
	gopath := pathList(a.Env["GOPATH"])

	if p := a.Env["GOROOT"]; p != "" {
		roots = append(roots, filepath.Join(p, "pkg", osArchSfx))
	}

	for _, p := range gopath {
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

	bestPath := findBestPath(gopath, a.Dir)

	log, _ := os.Create("D:\\Desktop\\gs.log")
	defer log.Close()

	for path, fn := range a.imports() {
		var vendor string

		if path[0] == '.' && len(bestPath) != 0 {
			// relative package path
			path = filepath.Join(a.Dir, path)
			fn = filepath.Join(a.Dir, fn)
			path = path[len(bestPath):]
			fn = fn[len(bestPath):]

		} else if len(bestPath) != 0 && pathExists(filepath.Join(bestPath, path)) == false {
			vendor = findVendor(bestPath, a.Dir, path)
		}

		if pathExists(goSrc + path) {
			// continue
		}

		log.WriteString(fmt.Sprintf("fn: %v\n", fn))
		log.WriteString(fmt.Sprintf("dir: %v\n", a.Dir))
		log.WriteString(fmt.Sprintf("path: %v\n", path))
		log.WriteString(fmt.Sprintf("vendor: %v\n", vendor))
		log.WriteString(fmt.Sprintf("vendorArchiveOk: %v\n", vendorArchiveOk(roots, strings.Replace(vendor, bestPath, "", 1) + ".a")))

		if alwaysInstall || !archiveOk(fn) || !vendorArchiveOk(roots, strings.Replace(vendor, bestPath, "", 1) + ".a") {
			var cmd *exec.Cmd
			// cmd.Dir = a.Dir

			switch {
				case len(vendor) != 0:
				// case pathExists(filepath.Join(a.Dir, "vendor", path)):
					cmd = exec.Command("go", "install")
					cmd.Dir = vendor

				case sfx == "":
					cmd = exec.Command("go", "install", path)

				default:
					cmd = exec.Command("go", "install", "-installsuffix", sfx, path)
			}

			cmd.Env = el
			cmd.Stderr = ioutil.Discard
			cmd.Stdout = ioutil.Discard
			log.WriteString(fmt.Sprintf("args: %v\n", cmd.Args))
			cmd.Run()

			if alwaysInstall == false && archiveOk(fn) {
				installed = append(installed, path)
			}

		}

		log.WriteString(fmt.Sprintf("\n"))
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
