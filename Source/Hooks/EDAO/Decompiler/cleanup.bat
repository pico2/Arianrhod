@for /F "delims=" %%i IN ('dir/b/s "%~dp0\__pycache__"') do rd/s/q "%%i" >NUL 2>NUL

