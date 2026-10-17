@echo off
setlocal
python -c "import sys" >nul 2>&1
if %ERRORLEVEL% equ 0 (
    python "%~dp000_Sistema\Engine\chat_merfi.py" %*
    goto :eof
)
py -3 -c "import sys" >nul 2>&1
if %ERRORLEVEL% equ 0 (
    py -3 "%~dp000_Sistema\Engine\chat_merfi.py" %*
    goto :eof
)
echo.
echo ================================================================================
echo   [AVISO] No se detecto un interprete de Python activo en tu sistema.
echo ================================================================================
echo   Para solucionar esto de inmediato:
echo   1. Ejecuta el archivo "INSTALADOR_AUTOMATICO_MERFI.cmd" (incluido en esta boveda).
echo   2. O instala Python 3.10+ desde: https://www.python.org/
echo      (Asegurate de marcar la casilla: "Add python.exe to PATH").
echo ================================================================================
echo.
pause
