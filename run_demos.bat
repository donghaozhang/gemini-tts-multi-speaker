@echo off
echo Loading environment variables from .env file...
for /f "delims=" %%x in (.env) do (set "%%x")

echo.
echo Select a demo to run:
echo 1. Gemini TTS basic examples
echo 2. Multi-speaker conversation demos
echo 3. Academic paper presentations
echo 4. Run all demos
echo.
set /p option=Enter choice ^(1-4^):

if "%option%"=="1" (
    echo Running Gemini TTS Example...
    python gemini_tts_example.py
) else if "%option%"=="2" (
    echo Running Multi-Speaker Demo...
    python multi_speaker_demo.py
) else if "%option%"=="3" (
    echo Running Academic Papers Demo...
    python academic_papers_demo.py
) else if "%option%"=="4" (
    echo Running Gemini TTS Example...
    python gemini_tts_example.py
    echo.
    echo Running Multi-Speaker Demo...
    python multi_speaker_demo.py
    echo.
    echo Running Academic Papers Demo...
    python academic_papers_demo.py
) else (
    echo Invalid choice.
)

pause
