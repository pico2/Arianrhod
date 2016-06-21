@echo off
cd/d "%~dp0"

rd/q VAXAutoText
rd/q VCUserProps

mklink /j VAXAutoText       "%appdata%\VisualAssist\Autotext"
mklink /j VCUserProps       "%LOCALAPPDATA%\Microsoft\MSBuild\v4.0"
mklink /j ImmPyCommands     "D:\Dev\Crack\Immunity Debugger\PyCommands"
mklink /j ImmPyLibs         "D:\Dev\Crack\Immunity Debugger\Libs"
mklink /j PyLibs            "D:\Dev\Python\Lib\site-packages"
rem mklink /j GoLibs            "D:\Dev\Go\pkgs"
mklink /j OllyDbgFuncInfo   "D:\Dev\Crack\Immunity Debugger\info"
mklink /j Source            "D:\Desktop\Source"
mklink /j Library           "D:\Dev\Library"
