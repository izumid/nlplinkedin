@echo off
TITLE PIP: INSTALL

set "path_env=%~dp0..\venv\Scripts"
echo Enviroment path: %path_env%

call "%path_env%\activate.bat"
python -m pip list
python -m pip install -U pip
python -m pip install -r "%~dp0../requirements.txt"
python -m pip list
call "%path_env%\deactivate.bat"

timeout 5