# Project Structure

## Overview
This repository contains a comprehensive Gemini API Text-to-Speech system with multi-speaker capabilities, organized for easy development and deployment.

## Directory Structure

```
notebook_peter/
├── .git/                           # Git repository
├── .env                           # Environment variables (API key)
├── .env.example                   # Example environment file
├── .gitignore                     # Git ignore rules
├── README.md                      # Main documentation
├── requirements.txt               # Python dependencies
├── PROJECT_STRUCTURE.md           # This file
│
├── Core Python Files:
├── gemini_tts_example.py          # Main TTS functions
├── multi_speaker_demo.py          # Multi-speaker demo scenarios
├── academic_papers_demo.py        # Academic paper presentations
├── full_papers_generator.py       # Full paper audio generator
│
├── Batch Scripts:
├── run_example.bat                # Run basic TTS examples
├── run_multi_speaker_demo.bat     # Run conversation demos
├── run_academic_papers_demo.bat   # Run academic presentations
│
└── result/                        # Generated audio files (16 files)
    ├── basic_example.wav          # Basic TTS demo
    ├── cheerful_example.wav       # Styled TTS demo
    ├── mysterious_example.wav     # Whisper style demo
    ├── casual_chat.wav            # Friends conversation
    ├── tech_discussion.wav        # Technical discussion
    ├── styled_conversation.wav    # Emotional dialogue
    ├── podcast_demo.wav           # Professional podcast
    ├── customer_service_demo.wav  # Support call scenario
    ├── teacher_student_demo.wav   # Educational interaction
    ├── interview_demo.wav         # Job interview scenario
    ├── story_dialogue_demo.wav    # Character dialogue
    ├── gneiss_web_paper.wav       # Academic paper 1
    ├── code_comment_paper.wav     # Academic paper 2
    ├── fineweb_paper.wav          # Academic paper 3
    ├── datacomp_lm_paper.wav      # Academic paper 4
    └── refined_web_paper.wav      # Academic paper 5
```

## Key Features

### 🔧 Environment Management
- **`.env` file**: Secure API key storage
- **`.env.example`**: Template for new users
- **Updated batch scripts**: Automatically load environment variables

### 📁 File Organization
- **Source code**: All Python files in root directory
- **Generated audio**: All WAV files organized in `result/` folder
- **Documentation**: Clear README and structure documentation

### 🎯 Git Repository
- **Initialized**: Ready for version control
- **Proper .gitignore**: Excludes sensitive files and large audio files
- **Initial commit**: All source code committed
- **Audio files excluded**: WAV files not tracked (too large)

### 🎤 TTS Capabilities
- **Single-speaker**: 30+ voice options with style control
- **Multi-speaker**: Conversation scenarios with 2 speakers
- **Academic content**: Research paper presentations
- **Batch processing**: Easy-to-run demo scripts

## Usage

### Quick Start
1. Copy `.env.example` to `.env` and add your API key
2. Install dependencies: `pip install -r requirements.txt`
3. Run demos using the batch files

### Development
- All source code is version controlled
- Audio outputs are organized in `result/` folder
- Environment variables managed securely
- Easy to extend with new scenarios

## Security
- API keys stored in `.env` file (not tracked by git)
- Sensitive files excluded via `.gitignore`
- Example configuration provided for new users

## Generated Content
- **16 audio files** totaling ~35MB
- **5 academic paper presentations**
- **6 conversation scenarios**
- **5 single-speaker style examples**

This structure provides a clean, organized, and secure foundation for TTS development and experimentation. 