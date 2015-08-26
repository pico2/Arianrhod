
// XXX: The documentation is duplicated here and in the the doc variable
// below. Update both at the same time.

// Command genqrc packs resource files into the Go binary.
//
// Usage: genqrc [options] <subdir1> [<subdir2> ...]
//
// The genqrc tool packs all resource files under the provided subdirectories into
// a single qrc.go file that may be built into the generated binary. Bundled files
// may then be loaded by Go or QML code under the URL "qrc:///some/path", where
// "some/path" matches the original path for the resource file locally.
//
// For example, the following will load a .qml file from the resource pack, and
// that file may in turn reference other content (code, images, etc) in the pack:
//
//     component, err := engine.LoadFile("qrc://path/to/file.qml")
//
// Starting with Go 1.4, this tool may be conveniently run by the "go generate"
// subcommand by adding a line similar to the following one to any existent .go
// file in the project (assuming the subdirectories ./code/ and ./images/ exist):
//
//     //go:generate genqrc code images
//
// Then, just run "go generate" to update the qrc.go file.
//
// During development, the generated qrc.go can repack the filesystem content at
// runtime to avoid the process of regenerating the qrc.go file and rebuilding the
// application to test every minor change made. Runtime repacking is enabled by
// setting the QRC_REPACK environment variable to 1:
//
//     export QRC_REPACK=1
//
// This does not update the static content in the qrc.go file, though, so after
// the changes are performed, genqrc must be run again to update the content that
// will ship with built binaries.
package main

import (
    "flag"
    "fmt"
    "io/ioutil"
    "os"
    "path/filepath"
    "text/template"
    "compress/zlib"
    "bytes"

    "goqml"
)

const doc = `
Usage: genqrc [options] <subdir1> [<subdir2> ...]

The genqrc tool packs all resource files under the provided subdirectories into
a single qrc.go file that may be built into the generated binary. Bundled files
may then be loaded by Go or QML code under the URL "qrc:///some/path", where
"some/path" matches the original path for the resource file locally.

For example, the following will load a .qml file from the resource pack, and
that file may in turn reference other content (code, images, etc) in the pack:

    component, err := engine.LoadFile("qrc://path/to/file.qml")

Starting with Go 1.4, this tool may be conveniently run by the "go generate"
subcommand by adding a line similar to the following one to any existent .go
file in the project (assuming the subdirectories ./code/ and ./images/ exist):

    //go:generate genqrc code images

Then, just run "go generate" to update the qrc.go file.

During development, the generated qrc.go can repack the filesystem content at
runtime to avoid the process of regenerating the qrc.go file and rebuilding the
application to test every minor change made. Runtime repacking is enabled by
setting the QRC_REPACK environment variable to 1:

    export QRC_REPACK=1

This does not update the static content in the qrc.go file, though, so after
the changes are performed, genqrc must be run again to update the content that
will ship with built binaries.
`

// XXX: The documentation is duplicated here and in the the package comment
// above. Update both at the same time.

var packageName = flag.String("package", "resource", "package name that qrc.go will be under (not needed for go generate)")

func main() {
    flag.Usage = func() {
        fmt.Fprintf(os.Stderr, "%s", doc)
        flag.PrintDefaults()
    }
    flag.Parse()
    if err := run(); err != nil {
        fmt.Fprintf(os.Stderr, "error: %v\n", err)
        os.Exit(1)
    }
}

func run() error {
    subdirs := flag.Args()
    if len(subdirs) == 0 {
        return fmt.Errorf("must provide at least one subdirectory path")
    }

    var rp qml.ResourcesPacker

    for _, subdir := range flag.Args() {
        subdir, err := filepath.Abs(subdir)
        if err != nil {
            return err
        }
        err = filepath.Walk(subdir, func(path string, info os.FileInfo, err error) error {
            if err != nil {
                return err
            }
            if info.IsDir() {
                return nil
            }

            data, err := ioutil.ReadFile(path)
            if err != nil {
                return err
            }

            respath := filepath.ToSlash(path)[len(filepath.Dir(subdir)) + 1:]
            println(respath)

            rp.Add(respath, data)
            return nil
        })
        if err != nil {
            return err
        }
    }

    resdata := rp.Pack().Bytes()
    compressed := bytes.NewBuffer(nil)

    compressResData := func (resdata []byte, w *bytes.Buffer) error {
        compreesor, err := zlib.NewWriterLevel(w, zlib.BestCompression)
        defer compreesor.Close()
        if err != nil {
            return err
        }

        _, err = compreesor.Write(resdata)
        if err != nil {
            return err
        }

        return nil
    }

    err := compressResData(resdata, compressed)
    if err != nil {
        return err
    }

    resdata = compressed.Bytes()

    f, err := os.Create("resource.go")
    if err != nil {
        return err
    }
    defer f.Close()

    data := templateData{
        PackageName:   *packageName,
        SubDirs:       subdirs,
        ResourcesData: resdata,
    }

    // $GOPACKAGE is set automatically by go generate.
    if pkgname := os.Getenv("GOPACKAGE"); pkgname != "" {
        data.PackageName = pkgname
    }

    err = tmpl.Execute(f, data)
    if err != nil {
        return err
    }

    f.WriteString("    ")

    count := 0
    for _, ch := range resdata {
        _, err = f.WriteString(fmt.Sprintf("0x%02X,", ch))
        count++

        if err == nil && count == 16 {
            count = 0
            _, err = f.WriteString("\n    ")
        }

        if err != nil {
            break
        }
    }

    _, err = f.WriteString("\n}")

    return err
}

type templateData struct {
    PackageName   string
    SubDirs       []string
    ResourcesData []byte
}

func buildTemplate(name, content string) *template.Template {
    return template.Must(template.New(name).Parse(content))
}

var tmpl = buildTemplate("qrc.go", `package {{.PackageName}}

// This file is automatically generated by gopkg.in/qml.v1/cmd/genqrc

import (
    "os"
    "bytes"
    "path/filepath"
    "io/ioutil"
    "compress/zlib"
    "goqml"
)

func init() {
    var r *qml.Resources
    var err error

    resdata := uncompressResource()
    resdata = repackResources()

    r, err = qml.ParseResources(resdata)
    if err != nil {
        panic("cannot parse bundled resources data: " + err.Error())
    }

    qml.LoadResources(r)
}

func uncompressResource() []byte {
    uncompressor, err := zlib.NewReader(bytes.NewReader(qrcResourcesData))
    if err != nil {
        panic(err.Error())
    }

    defer uncompressor.Close()

    resdata, err := ioutil.ReadAll(uncompressor)
    if err != nil {
        panic(err.Error())
    }

    qrcResourcesData = nil
    return resdata
}

func repackResources() []byte {
    subdirs := {{printf "%#v" .SubDirs}}
    var rp qml.ResourcesPacker
    for _, subdir := range subdirs {
        subdir, err := filepath.Abs(subdir)
        if err != nil {
            panic("[repackResources] get fullpath of subdir failed: " + err.Error())
        }
        err = filepath.Walk(subdir, func(path string, info os.FileInfo, err error) error {
            if err != nil {
                return err
            }
            if info.IsDir() {
                return nil
            }
            data, err := ioutil.ReadFile(path)
            if err != nil {
                return err
            }

            respath := filepath.ToSlash(path)[len(filepath.Dir(subdir)) + 1:]

            rp.Add(respath, data)
            return nil
        })
        if err != nil {
            panic("[repackResources] walk subdir '" + subdir + "' failed: " + err.Error())
        }
    }
    return rp.Pack().Bytes()
}

var qrcResourcesData = []byte{
`)
