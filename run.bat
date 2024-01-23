@echo off
echo installing libraries...
pip install -r requirements.txt >nul || py -m pip install -r requirements.txt >nul || python -m pip install -r requirements.txt >nul || python3 -m pip install -r requirements.txt >nul
cls
echo Launching Coin's Tool, Please Wait.
timeout /t 5 /NOBREAK >nul
py run.py || python run.py || python3 run.py
pause
