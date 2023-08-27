@echo off
set toAdd=%~dp0
setx /m "path" "%toAdd%;%path%"
pause

