# Gemini API Text-to-Speech Example

A simple Python example demonstrating how to use Google's Gemini API for text-to-speech generation, based on the [official documentation](https://ai.google.dev/gemini-api/docs/speech-generation?authuser=3).

## Features

- 🎤 **Single-speaker TTS**: Convert text to speech with 30 different voice options
- 👥 **Multi-speaker TTS**: Create conversations between 2 people with different voices
- 🎨 **Style Control**: Use natural language to control tone, pace, and emotion
- 📁 **WAV Output**: Save generated speech as high-quality WAV files
- 🛡️ **Error Handling**: Robust error handling and user feedback
- 🎭 **Real-world Examples**: Podcast, customer service, education, and interview scenarios

## Prerequisites

1. **Google AI API Key**: Get your API key from [Google AI Studio](https://aistudio.google.com/)
2. **Python 3.7+**: Make sure you have Python installed

## Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your API key** using one of these methods:

   **Method 1: Using .env file (Recommended)**
   ```bash
   # Create a .env file in the project root
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

   **Method 2: Environment variable**
   ```bash
   # On Windows
   set GEMINI_API_KEY=your_api_key_here
   
   # On macOS/Linux
   export GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Basic Usage

```python
from gemini_tts_example import text_to_speech_simple

# Simple text-to-speech
text_to_speech_simple(
    text="Hello, this is a test of Gemini TTS!",
    voice_name="Kore",
    output_file="my_speech.wav"
)
```

### With Style Control

```python
from gemini_tts_example import text_to_speech_with_style

# Text-to-speech with emotional style
text_to_speech_with_style(
    text="Welcome to the future of AI!",
    style_instruction="Say excitedly and enthusiastically:",
    voice_name="Puck",
    output_file="excited_speech.wav"
)
```

### Multi-Speaker Conversations

```python
from gemini_tts_example import text_to_speech_multi_speaker

# Create a conversation between two people
dialogue = """Alice: Hey Bob! Did you hear about the new AI features?

Bob: Yes! The text-to-speech quality is incredible!

Alice: I know, right? It sounds so natural and expressive."""

speakers = [
    {"name": "Alice", "voice": "Leda"},   # Youthful
    {"name": "Bob", "voice": "Puck"}     # Upbeat  
]

text_to_speech_multi_speaker(dialogue, speakers, "conversation.wav")
```

### Run Examples

```bash
# Run all examples (single and multi-speaker)
python gemini_tts_example.py

# Run only multi-speaker demos
python multi_speaker_demo.py
```

On Windows you can launch these examples from the interactive
`run_demos.bat` script.

**Single-speaker examples:**
- `basic_example.wav` - Basic TTS
- `cheerful_example.wav` - Cheerful style
- `mysterious_example.wav` - Mysterious whisper

**Multi-speaker examples:**
- `tech_discussion.wav` - Tech podcast conversation
- `casual_chat.wav` - Friends chatting
- `styled_conversation.wav` - Emotional dialogue

**Multi-speaker demo scenarios:**
- `podcast_demo.wav` - Professional podcast
- `customer_service_demo.wav` - Support call
- `teacher_student_demo.wav` - Educational interaction
- `interview_demo.wav` - Job interview scenario

## Available Voices

The API supports 30 different voices with various characteristics:

| Voice | Style | Voice | Style |
|-------|-------|-------|-------|
| **Kore** | Firm | **Puck** | Upbeat |
| **Zephyr** | Bright | **Charon** | Informative |
| **Enceladus** | Breathy | **Fenrir** | Excitable |
| **Aoede** | Breezy | **Leda** | Youthful |

[See full voice list in documentation](https://ai.google.dev/gemini-api/docs/speech-generation?authuser=3#voice-options)

## Supported Models

- `gemini-2.5-flash-preview-tts` - Fast, efficient TTS
- `gemini-2.5-pro-preview-tts` - High-quality TTS

## Supported Languages

The API automatically detects input language and supports 24 languages including:
- English (US, India)
- Spanish, French, German
- Japanese, Korean, Chinese
- Hindi, Arabic, Russian
- And many more...

## Style Control Examples

You can control speech style using natural language:

```python
# Different emotional styles
"Say cheerfully: Have a wonderful day!"
"Say in a spooky whisper: Something wicked this way comes"
"Say tiredly and bored: What's on the agenda today?"
"Say excitedly: You're never going to guess what happened!"
```

## Technical Details

- **Context Window**: 32k tokens
- **Audio Format**: 24kHz, 16-bit PCM, Mono WAV
- **API**: Google Gemini API with native TTS capabilities

## Troubleshooting

1. **API Key Error**: Make sure `GEMINI_API_KEY` environment variable is set
2. **Import Error**: Install dependencies with `pip install -r requirements.txt`
3. **Audio Issues**: Generated files are in WAV format - use any audio player

## References

- [Gemini API Speech Generation Documentation](https://ai.google.dev/gemini-api/docs/speech-generation?authuser=3)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Cookbook](https://github.com/google-gemini/cookbook)

## License

This example is provided for educational purposes. Please refer to Google's terms of service for API usage. 