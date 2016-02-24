set GOROOT=%~dp0
set GOPATH=%~dp0pkgs;D:\Desktop\Source\GoProject;D:\Desktop\Source\Project\Private;D:\Desktop\Source\Falcom
set PATH=%GOROOT%bin;%GOROOT%pkgs\bin;D:\Dev\PortableGit\bin;D:\Desktop\Source\GoProject\src\AppleIdRegister;%PATH%
set GOGCCFLAGS="-g -O3 -fPIC -m64 -pthread --gc-sections"
set CGO_ENABLED="1"
set CGO_ENABLED=1
::set CGO_CXXFLAGS="-O3"


if not exist "%~dp0bin32\" (
    set arch=x86
    set GOARCH=386
    set GO_PKG_ARCH=windows_386
    set "PATH=D:\Dev\mingw-w64\i686-5.1.0-posix-dwarf-rt_v4-rev0\mingw32\bin;%PATH%"
) else (
    set arch=amd64
    set GOARCH=amd64
    set GO_PKG_ARCH=windows_amd64
    set "PATH=D:\Dev\Library\Qt\mingw\mingw64\bin;%PATH%"
)

set "PATH=%GOROOT%pkgs\bin\%GO_PKG_ARCH%;%PATH%"

set "QT_PATH=D:\Dev\Library\Qt\mingw\%arch%"

set "QT_QPA_PLATFORM_PLUGIN_PATH=%QT_PATH%\plugins\platforms"
set "PKG_CONFIG_PATH=%QT_PATH%\lib\pkgconfig"
set "LIBRARY_PATH=%QT_PATH%\lib;%LIBRARY_PATH%"
set "CPATH=%QT_PATH%\include;%CPATH%"
set "PATH=%QT_PATH%\bin;%PATH%"

goto:eof

if not exist "%~dp0bin32\" (
    set "PKG_CONFIG_PATH=D:\Dev\Library\Qt\Qt5.5.0\5.5\mingw492_32\lib\pkgconfig"
    set "LIBRARY_PATH=D:\Dev\Library\Qt\Qt5.5.0\5.5\mingw492_32\lib;%LIBRARY_PATH%"
    set "CPATH=D:\Dev\Library\Qt\Qt5.5.0\5.5\mingw492_32\include;%CPATH%"
    set "PATH=D:\Dev\Library\Qt\Qt5.5.0\5.5\mingw492_32\bin;D:\Dev\mingw-w64\i686-5.1.0-posix-dwarf-rt_v4-rev0\mingw32\bin;%PATH%"
) else (
    set "PKG_CONFIG_PATH=D:\Dev\Library\Qt\qt-5.5.0-x64-mingw510r0-seh-rev0\qt-5.5.0-x64-mingw510r0-seh-rev0\lib\pkgconfig"
    set "LIBRARY_PATH=D:\Dev\Library\Qt\qt-5.5.0-x64-mingw510r0-seh-rev0\qt-5.5.0-x64-mingw510r0-seh-rev0\lib;%LIBRARY_PATH%"
    set "CPATH=D:\Dev\Library\Qt\qt-5.5.0-x64-mingw510r0-seh-rev0\qt-5.5.0-x64-mingw510r0-seh-rev0\include;%CPATH%"
    set "PATH=D:\Dev\Library\Qt\qt-5.5.0-x64-mingw510r0-seh-rev0\qt-5.5.0-x64-mingw510r0-seh-rev0\bin;D:\Dev\Library\Qt\qt-5.5.0-x64-mingw510r0-seh-rev0\mingw64\bin;%PATH%"
)
