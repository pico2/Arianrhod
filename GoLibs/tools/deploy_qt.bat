@echo off
cd/d "%~dp0"

call init.bat

set "TARGET=%~dp1bin"
md "%TARGET%"

copy "%~dpn1.exe" "%TARGET%"

for %%i in (Qt5Core.dll ^
            Qt5Gui.dll ^
            Qt5Qml.dll ^
            Qt5Quick.dll ^
            Qt5Widgets.dll ^
            Qt5Network.dll ^
            libgcc_s_dw2-1.dll ^
            libstdc++-6.dll ^
            libwinpthread-1.dll ^
            libgcc_s_seh-1.dll
    ) do (
    copy "%QT_PATH%\bin\%%i" "%TARGET%"
)

md "%TARGET%\platforms"
copy "%QT_PATH%\plugins\platforms\qwindows.dll" "%TARGET%\platforms"

::echo D | xcopy /E /Y "%QT_PATH%\qml\QtQml" "%TARGET%\QtQml"
echo D | xcopy /E /Y "%QT_PATH%\qml\QtQuick" "%TARGET%\QtQuick"
echo D | xcopy /E /Y "%QT_PATH%\qml\QtQuick.2" "%TARGET%\QtQuick.2"
