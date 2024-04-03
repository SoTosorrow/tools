@echo off

@REM set yourself chrome path
set chromePath="C:\Program Files\Google\Chrome\Application\chrome.exe"

if not exist "%chromePath%" (
    echo "Chrome not found."
    exit /b
)

@REM echo %CD%
%chromePath% %CD%/%1