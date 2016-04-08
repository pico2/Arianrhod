# Microsoft Developer Studio Project File - Name="QQ2011" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Dynamic-Link Library" 0x0102

CFG=QQ2011 - Win32 Release
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "QQ2011.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "QQ2011.mak" CFG="QQ2011 - Win32 Release"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "QQ2011 - Win32 Release" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=cl.exe
MTL=midl.exe
RSC=rc.exe
# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "Release"
# PROP BASE Intermediate_Dir "Release"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "Release"
# PROP Intermediate_Dir "Release"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MT /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "QQ2011_EXPORTS" /YX /FD /c
# ADD CPP /nologo /Gr /MD /W4 /GR- /O2 /Ob1 /D "WIN32" /D "NDEBUG" /FD /GL /GS- /arch:SSE /MP /c
# ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0x804 /d "NDEBUG"
# ADD RSC /l 0x804 /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /machine:I386
# ADD LINK32 mylib.lib undoc_ntdll.lib ntdll.lib kernel32.lib user32.lib gdi32.lib gdiplus.lib shell32.lib /nologo /dll /pdb:"wtsapi32.pdb" /debug /machine:I386 /out:"D:\Software\QQ\Bin\zlib.dll" /LTCG /OPT:REF
# SUBTRACT LINK32 /pdb:none
# Begin Target

# Name "QQ2011 - Win32 Release"
# Begin Group "Hooks"

# PROP Default_Filter ""
# Begin Source File

SOURCE=.\Hooks\HookAppFramework.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookAppMisc.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookAppUtil.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookCamera.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookCommon.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookGdi32.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookGroupApp.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookIM.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookKernelUtil.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookMainFrame.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookMsgMgr.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookNtdll.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookPsapi.cpp
# End Source File
# Begin Source File

SOURCE=.\Hooks\Hooks.h
# End Source File
# Begin Source File

SOURCE=.\Hooks\HookUser32.cpp
# End Source File
# End Group
# Begin Source File

SOURCE=.\QQ2011.cpp
# End Source File
# Begin Source File

SOURCE=.\QQ2011.h
# End Source File
# Begin Source File

SOURCE=.\QQMethod.h
# End Source File
# End Target
# End Project
