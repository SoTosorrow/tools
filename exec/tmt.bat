@echo off
set path=%~dp0
cd /d %path%
cd ..

set pythonPath="D:\Python\python.exe"
if not exist %pythonPath% (
    echo "Python not found."
    exit /b 1
)
%pythonPath% py/api_tencent_tmt.py %1
