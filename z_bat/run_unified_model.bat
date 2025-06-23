@echo off
TITLE RUN PROG: 05_unified_models_3.5.0

set "path_env=%~dp0..\Scripts"
echo Enviroment path: %path_env%

call "%path_env%\activate.bat"
call "%~dp0Scripts\python.exe" "%~dp005_unified_models_3.5.0.py" /popup
call "%path_env%\deactivate.bat"

echo "SUCCESSFUL"

pause