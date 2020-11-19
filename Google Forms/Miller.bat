@echo off
:: CHCP 65001 is required to send Hebrew characters!!!
CHCP 65001 >null
cd "%~dp0"

python health-form.py "Sagie" "שגיא מילר" "4" "רחלי"
python health-form.py "Rotem" "רתם מילר" "2" "רחלי"

echo.
echo Done
pause