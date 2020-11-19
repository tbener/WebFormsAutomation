@echo off
:: CHCP 65001 is required to send Hebrew characters!!!
CHCP 65001 
cd "%~dp0"
date /t
time /t
echo.

python health-form.py "Adi" "עדי בנר" "4" "טל"
python health-form.py "Maayan" "מעיין בנר" "2" "טל"

echo.
echo Done
pause