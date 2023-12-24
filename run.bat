@echo off
echo installing libraries...
pip install -r requirements.txt
cls
echo Launching Coln's Tool, Please Wait.
timeout /t 5
py run.py
