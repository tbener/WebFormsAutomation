@echo off
:: CHCP 65001 is required to send Hebrew characters!!!
CHCP 65001 >null
cd "%~dp0"

for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo Current time is %mydate% %mytime%

:: USAGE:
:: python health-form.py "KidNameInEnglish" "KidName" "GradeNumber" "Parent"
python health-form.py "Adi" "עדי בנר" "4" "טל"
python health-form.py "Maayan" "מעיין בנר" "2" "טל"

echo.
echo Done
pause