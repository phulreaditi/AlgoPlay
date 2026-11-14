@echo off
echo Starting AlgoPlay - Interactive Algorithm Visualizer...
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred while launching AlgoPlay.
    echo Ensure Python 3.10+ is installed and available in PATH.
    pause
)
