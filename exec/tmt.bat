@echo off

@REM setlocal
@REM 当前脚本所在目录
set path=%~dp0
cd /d %path%
cd ..

set pythonPath="D:\Python\python.exe"
if not exist %pythonPath% (
    echo "Python not found."
    exit /b 1
)
%pythonPath% py/api_tencent_tmt.py %1
