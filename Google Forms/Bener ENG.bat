@echo off
CHCP 65001 >null
cd "%~dp0"

python health-form.py "Adi" "Adi Bener" "4" "Tal"
python health-form.py "Maayan" "Maayan Bener" "2" "Tal"

echo.
echo Done
pause