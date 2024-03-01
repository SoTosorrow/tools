@echo off
set path=%~dp0
cd /d %path%
cd ..
"D:\Python\python.exe" py/api_tencent_tmt.py %1
