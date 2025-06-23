@echo off
TITLE PIP: INSTALL

set "path_env=%~dp0..\Scripts"
echo Enviroment path: %path_env%

call "%path_env%\activate.bat"
python -m pip list
python -m pip install -U pip
python -m pip install beautifulsoup4
python -m pip install wordcloud
python -m pip install matplotlib
rem python -m pip install pandas
rem python -m pip install seaborn

python -m pip list
call "%path_env%\deactivate.bat"

pause