@echo off
:: CHCP 65001 is required to send Hebrew characters!!!
CHCP 65001 
cd "%~dp0"

venv\scripts\python smart-school.py

pause