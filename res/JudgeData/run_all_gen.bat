@echo off
setlocal enabledelayedexpansion

echo Starting batch generation from P67 to P132...

for /L %%i in (67,1,132) do (
    set "PROBLEM_DIR=P%%i"
    
    if exist "!PROBLEM_DIR!" (
        echo Processing !PROBLEM_DIR!...
        
        pushd "!PROBLEM_DIR!"
        
        if exist "gen.py" (
            python gen.py
            if !errorlevel! neq 0 (
                echo.
                echo [ERROR] gen.py failed in !PROBLEM_DIR!
                echo.
                pause
            ) else (
                echo [SUCCESS] !PROBLEM_DIR! generated.
            )
        ) else (
            echo [WARNING] gen.py not found in !PROBLEM_DIR!, skipping.
        )
        
        popd
    ) else (
        echo [INFO] Directory !PROBLEM_DIR! does not exist, skipping.
    )
)

echo.
echo All done.
pause
