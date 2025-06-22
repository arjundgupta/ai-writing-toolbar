@echo off
echo Starting VibeType API...
echo.

REM Check if OpenAI API key is set
if "%OPENAI_API_KEY%"=="" (
    echo ERROR: OPENAI_API_KEY environment variable is not set!
    echo Please set it first:
    echo set OPENAI_API_KEY=your-openai-api-key-here
    echo.
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Installing dependencies...
pip install -r requirements.txt

REM Start the API
echo.
echo Starting API server...
echo API will be available at: http://localhost:8000
echo API docs at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

pause
