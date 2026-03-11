@echo off
setlocal enabledelayedexpansion

echo Cleaning .exe files from P67 to P132...

for /L %%i in (67,1,132) do (
    set "PROBLEM_DIR=P%%i"
    
    if exist "!PROBLEM_DIR!" (
        echo Cleaning !PROBLEM_DIR!...
        if exist "!PROBLEM_DIR!\*.exe" (
            del /q "!PROBLEM_DIR!\*.exe"
            echo   - Deleted .exe files
        ) else (
            echo   - No .exe files found
        )
    )
)

echo.
echo Cleanup complete.
pause
