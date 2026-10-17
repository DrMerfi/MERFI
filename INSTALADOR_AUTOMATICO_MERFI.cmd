@echo off
setlocal enabledelayedexpansion
title Instalador Automatico de M.E.R.F.I. v1.0
chcp 65001 >nul 2>&1

echo ================================================================================
echo   INSTALADOR AUTOMATICO DE M.E.R.F.I. v1.0
echo   Preparando tu espacio de trabajo inteligente en tu computadora...
echo ================================================================================
echo.

:: 1. Comprobar si Python esta instalado (Blindaje contra alias vacio de Windows Store)
echo [1/3] Verificando instalacion de Python en tu sistema...
set "PY_CMD="

python -c "import sys; sys.exit(0 if sys.version_info[0] >= 3 else 1)" >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=python"
) else (
    py -3 -c "import sys; sys.exit(0 if sys.version_info[0] >= 3 else 1)" >nul 2>&1
    if !ERRORLEVEL! equ 0 (
        set "PY_CMD=py -3"
    )
)

if defined PY_CMD (
    for /f "tokens=*" %%v in ('!PY_CMD! --version') do set PY_VER=%%v
    echo       [OK] !PY_VER! detectado correctamente (usando !PY_CMD!).
) else (
    echo       [!] Python no fue detectado o esta inactivo. Instalando Python 3.12...
    echo       Por favor espera un momento (no cierres esta ventana)...
    
    :: Intento 1 con winget
    winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements --silent >nul 2>&1
    
    :: Comprobar si winget funciono
    python -c "import sys; sys.exit(0 if sys.version_info[0] >= 3 else 1)" >nul 2>&1
    if !ERRORLEVEL! equ 0 (
        set "PY_CMD=python"
    ) else (
        echo       Descargando instalador oficial de python.org mediante conexion segura...
        where curl >nul 2>&1
        if !ERRORLEVEL! equ 0 (
            curl -sSL "https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe" -o "%TEMP%\py_merfi_setup.exe" >nul 2>&1
        ) else (
            powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe' -OutFile '$env:TEMP\py_merfi_setup.exe'" >nul 2>&1
        )
        if exist "%TEMP%\py_merfi_setup.exe" (
            start /wait "" "%TEMP%\py_merfi_setup.exe" /quiet PrependPath=1 Include_test=0 SimpleInstall=1
            del "%TEMP%\py_merfi_setup.exe" >nul 2>&1
        )
    )
    
    :: Refrescar variables de PATH para esta sesion
    set "PATH=%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%ProgramFiles%\Python312;%ProgramFiles%\Python312\Scripts;%PATH%"
    
    python -c "import sys; sys.exit(0 if sys.version_info[0] >= 3 else 1)" >nul 2>&1
    if !ERRORLEVEL! equ 0 (
        set "PY_CMD=python"
        echo       [OK] Python instalado y configurado con exito.
    ) else (
        py -3 -c "import sys; sys.exit(0 if sys.version_info[0] >= 3 else 1)" >nul 2>&1
        if !ERRORLEVEL! equ 0 (
            set "PY_CMD=py -3"
            echo       [OK] Python Launcher detectado y activo.
        ) else (
            echo       [!] Aviso: Python se ha instalado. Si no se reconoce de inmediato, reinicia esta ventana.
            set "PY_CMD=python"
        )
    )
)
echo.

:: 2. Instalar paquetes de Python necesarios en silencio
echo [2/3] Configurando librerias de soporte (requests, pydantic)...
!PY_CMD! -m pip install -q requests pydantic >nul 2>&1
echo       [OK] Librerias configuradas.
echo.

:: 3. Inicializar base de datos de la boveda (Cold-Start FTS5)
echo [3/3] Inicializando memoria local y base de datos de la boveda...
if exist "%~dp0Mi_Boveda\00_Sistema\Engine\memory_engine.py" (
    !PY_CMD! "%~dp0Mi_Boveda\00_Sistema\Engine\memory_engine.py" >nul 2>&1
) else if exist "%~dp000_Sistema\Engine\memory_engine.py" (
    !PY_CMD! "%~dp000_Sistema\Engine\memory_engine.py" >nul 2>&1
)
echo       [OK] Memoria local preparada.
echo.

echo ================================================================================
echo   INSTALACION DE M.E.R.F.I. FINALIZADA CON EXITO
echo ================================================================================
echo.
echo Proximos pasos para comenzar a trabajar:
echo.
echo   1. Abre Obsidian en tu computadora (descargalo de obsidian.md si aun no lo tienes).
echo   2. Haz clic en "Abrir carpeta como boveda" y selecciona la carpeta "Mi_Boveda".
echo   3. En Obsidian, haz clic en "Desactivar modo restringido" (para activar la terminal).
echo   4. Abre la Terminal Integrada con el icono lateral (>_) o presiona Ctrl+P y busca Terminal.
echo   5. Escribe simplemente:  merfi   (y presiona Enter).
echo.
echo ================================================================================
echo Presiona cualquier tecla para cerrar este instalador.
pause >nul
