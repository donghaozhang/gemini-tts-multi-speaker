@echo off
echo Loading environment variables from .env file...
for /f "delims=" %%x in (.env) do (set "%%x")

echo.
echo Running Academic Papers Multi-Speaker TTS Demo...
echo This will create audio presentations for 5 research papers:
echo - GneissWeb: High Quality Data for LLMs
echo - ML-LLM Code Comment Classification  
echo - FineWeb Datasets for Language Models
echo - DataComp-LM Training Set Benchmark
echo - RefinedWeb Dataset for Falcon LLM
echo.
echo Each paper will be presented by two narrators with different voices.
echo.

python academic_papers_demo.py

echo.
echo Academic papers demo completed!
echo Check the generated WAV files to hear the research presentations.
pause 