@ECHO ON
CD /D %~dp0
SET Program="C:\Users\mmyetisi\AppData\Local\LyX 2.1\bin\lyx.exe"
for %%A in (*.lyx) do %Program% --export  "latex"  %%A
python removelyx.py
Pause