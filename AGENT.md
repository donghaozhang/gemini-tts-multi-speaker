# Repository Overview

This AGENT file summarizes key information about the project for developers working with this repository.

## Completed Function
- **`text_to_speech_simple`** – Converts text to speech using the Gemini API and saves output as a WAV file. See `gemini_tts_example.py` lines 41–93.

## Tech Stack
- Python 3.7+
- [google-genai](https://pypi.org/project/google-genai/) library
- Google Gemini API for text-to-speech generation

## Coding Style
- Functions use snake_case names
- Docstrings in triple quotes
- Generally follows PEP 8 conventions

## File Structure
- `gemini_tts_example.py` – Core TTS functions
- `multi_speaker_demo.py` – Multi-speaker conversation demos
- `academic_papers_demo.py` – Academic paper presentations
- `full_papers_generator.py` – Generate full paper audio
- `requirements.txt` – Python dependencies
- `README.md` and `PROJECT_STRUCTURE.md` – Documentation

## TODOs
- Separate the sample dialogue text from the Python scripts into a JSON file for easier editing
