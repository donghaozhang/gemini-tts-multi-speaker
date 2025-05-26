@echo off
echo Loading environment variables from .env file...
for /f "delims=" %%x in (.env) do (set "%%x")

echo.
echo Running Multi-Speaker Text-to-Speech Demos...
echo This will create several conversation examples:
echo - Podcast conversation
echo - Customer service call
echo - Teacher-student interaction  
echo - Story dialogue
echo - Job interview
echo.

python multi_speaker_demo.py

echo.
echo Multi-speaker demos completed!
echo Check the generated WAV files to hear the conversations.
pause 