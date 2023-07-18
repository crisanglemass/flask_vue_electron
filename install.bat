@echo off

REM Check for Node.js
node -v > nul 2>&1
if %errorlevel% equ 0 (
echo Node.js is already installed!
) else (
echo Node.js is not installed. Please install it.
echo Visit https://nodejs.org/ to download and install Node.js.
echo After installation, please run this script again.
pause
)

REM Check for Python
python --version > nul 2>&1
if %errorlevel% equ 0 (
echo Python is already installed!
) else (
echo Python is not installed. Please install it.
echo Visit https://www.python.org/downloads/ to download and install Python.
echo After installation, please run this script again.
pause
)
echo Check complete!


echo create virtual environment
py -3.9 -m venv venv
venv\Scripts\python -m pip install -r requirements.txt


echo initial vue environment
call npm install --save
cd web
call npm install --save
call npm run build


