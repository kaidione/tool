@echo off
echo 添加allure环境变量
set regpath=HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
set Allure_Home=Allure_Home
set allurepath=%~dp0
reg add "%regpath%" /v %Allure_Home% /d %allurepath% /f
setx /m "path" "%%Allure_Home%%\bin;%path%"
pause>nul