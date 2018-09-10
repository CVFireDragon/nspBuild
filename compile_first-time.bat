@echo off
pip install pyinstaller
pyinstaller --icon=nspBuild.ico --onefile nspBuild.py
echo Done!
pause