
@echo off
echo Downloading and installing massdns for Windows...

set "MASSDNS_URL=https://github.com/blechschmidt/massdns/releases/latest/download/massdns.exe"
set "DEST=C:\Windows\System32\massdns.exe"

curl -L %MASSDNS_URL% -o massdns.exe
if exist massdns.exe (
    echo Moving massdns.exe to System32...
    move /Y massdns.exe %DEST%
    echo Done. Make sure C:\Windows\System32 is in your PATH.
) else (
    echo Failed to download massdns.exe
)
pause
