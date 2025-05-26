#!/usr/bin/env python3
"""
Simple example of using Google Gemini API for Text-to-Speech generation.

This example demonstrates how to convert text to speech using the Gemini API
and save the output as a WAV file. Supports both single-speaker and multi-speaker TTS.

Requirements:
- pip install google-genai
- Set your GEMINI_API_KEY environment variable

Supported models:
- gemini-2.5-flash-preview-tts
- gemini-2.5-pro-preview-tts
"""

import os
import wave
from google import genai
from google.genai import types
from dialogues import get_dialogue


def save_wave_file(filename, pcm_data, channels=1, rate=24000, sample_width=2):
    """
    Save PCM audio data to a WAV file.
    
    Args:
        filename (str): Output filename
        pcm_data (bytes): PCM audio data
        channels (int): Number of audio channels (default: 1 for mono)
        rate (int): Sample rate in Hz (default: 24000)
        sample_width (int): Sample width in bytes (default: 2)
    """
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm_data)


def text_to_speech_simple(text, voice_name="kore", output_file="output.wav"):
    """
    Convert text to speech using Gemini API.
    
    Args:
        text (str): Text to convert to speech
        voice_name (str): Voice to use (default: "Kore")
        output_file (str): Output filename (default: "output.wav")
    
    Available voices include:
    - Kore (Firm), Zephyr (Bright), Puck (Upbeat), Charon (Informative)
    - Fenrir (Excitable), Aoede (Breezy), Enceladus (Breathy), etc.
    """
    
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set the GEMINI_API_KEY environment variable")
    
    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)
    
    try:
        # Generate speech from text
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voice_name,
                        )
                    )
                ),
            )
        )
        
        # Extract audio data from response
        audio_data = response.candidates[0].content.parts[0].inline_data.data
        
        # Save to WAV file
        save_wave_file(output_file, audio_data)
        
        print(f"✅ Speech generated successfully!")
        print(f"📄 Text: {text}")
        print(f"🎤 Voice: {voice_name}")
        print(f"💾 Saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error generating speech: {e}")
        raise


def text_to_speech_with_style(text, style_instruction, voice_name="kore", output_file="styled_output.wav"):
    """
    Convert text to speech with style control using natural language prompts.
    
    Args:
        text (str): Text to convert to speech
        style_instruction (str): Style instruction (e.g., "Say cheerfully:", "Say in a whisper:")
        voice_name (str): Voice to use
        output_file (str): Output filename
    """
    
    # Combine style instruction with text
    full_prompt = f"{style_instruction} {text}"
    
    text_to_speech_simple(full_prompt, voice_name, output_file)


def text_to_speech_multi_speaker(dialogue_text, speakers_config, output_file="multi_speaker.wav"):
    """
    Convert dialogue text to speech with multiple speakers (up to 2 speakers).
    
    Args:
        dialogue_text (str): Dialogue text with speaker names (e.g., "Speaker1: Hello! Speaker2: Hi there!")
        speakers_config (list): List of dictionaries with speaker configuration
                               [{"name": "Speaker1", "voice": "Kore"}, {"name": "Speaker2", "voice": "Puck"}]
        output_file (str): Output filename
    
    Example speakers_config:
        [
            {"name": "Alice", "voice": "Kore", "style": "friendly"},
            {"name": "Bob", "voice": "Puck", "style": "excited"}
        ]
    """
    
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set the GEMINI_API_KEY environment variable")
    
    # Validate speakers (max 2 for multi-speaker TTS)
    if len(speakers_config) > 2:
        raise ValueError("Multi-speaker TTS supports maximum 2 speakers")
    if len(speakers_config) < 2:
        raise ValueError("Multi-speaker TTS requires at least 2 speakers")
    
    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)
    
    # Build speaker voice configurations
    speaker_voice_configs = []
    for speaker in speakers_config:
        speaker_voice_configs.append(
            types.SpeakerVoiceConfig(
                speaker=speaker["name"],
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=speaker["voice"]
                    )
                )
            )
        )
    
    try:
        # Generate multi-speaker speech
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=dialogue_text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                        speaker_voice_configs=speaker_voice_configs
                    )
                ),
            )
        )
        
        # Extract audio data from response
        audio_data = response.candidates[0].content.parts[0].inline_data.data
        
        # Save to WAV file
        save_wave_file(output_file, audio_data)
        
        print(f"✅ Multi-speaker speech generated successfully!")
        print(f"📄 Dialogue: {dialogue_text}")
        print(f"🎤 Speakers: {', '.join([f'{s['name']} ({s['voice']})' for s in speakers_config])}")
        print(f"💾 Saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error generating multi-speaker speech: {e}")
        raise


def create_dialogue_from_script(script_lines):
    """
    Helper function to create dialogue text from a list of script lines.
    
    Args:
        script_lines (list): List of tuples with (speaker_name, text)
                            [("Alice", "Hello there!"), ("Bob", "Hi Alice, how are you?")]
    
    Returns:
        str: Formatted dialogue text
    """
    dialogue_parts = []
    for speaker, text in script_lines:
        dialogue_parts.append(f"{speaker}: {text}")
    
    return "\n".join(dialogue_parts)


def main():
    """Main function demonstrating different TTS examples."""
    
    print("🎵 Gemini API Text-to-Speech Examples\n")
    
    # Example 1: Basic text-to-speech
    print("Example 1: Basic TTS")
    text1 = "Hello! This is a simple text-to-speech example using Google Gemini API."
    text_to_speech_simple(text1, voice_name="kore", output_file="basic_example.wav")
    print()
    
    # Example 2: With style control
    print("Example 2: TTS with style")
    text2 = "Welcome to the wonderful world of artificial intelligence!"
    text_to_speech_with_style(
        text2, 
        "Say cheerfully and enthusiastically:", 
        voice_name="puck",  # Upbeat voice
        output_file="cheerful_example.wav"
    )
    print()
    
    # Example 3: Different voice and style
    print("Example 3: Mysterious style")
    text3 = "In the depths of the digital realm, secrets await discovery."
    text_to_speech_with_style(
        text3,
        "Say in a mysterious whisper:",
        voice_name="enceladus",  # Breathy voice
        output_file="mysterious_example.wav"
    )
    print()
    
    # Example 4: Multi-speaker conversation - Tech discussion
    print("Example 4: Multi-speaker Tech Discussion")
    tech_dialogue = get_dialogue("gemini_tts_example", "tech_dialogue")
    
    tech_speakers = [
        {"name": "Dr. Sarah", "voice": "kore"},  # Firm, professional
        {"name": "Marcus", "voice": "charon"}    # Informative
    ]
    
    text_to_speech_multi_speaker(
        tech_dialogue, 
        tech_speakers, 
        "tech_discussion.wav"
    )
    print()
    
    # Example 5: Multi-speaker conversation - Casual chat
    print("Example 5: Multi-speaker Casual Chat")
    
    # Using the helper function to create dialogue
    casual_script = get_dialogue("gemini_tts_example", "casual_script")
    
    casual_dialogue = create_dialogue_from_script(casual_script)
    
    casual_speakers = [
        {"name": "Emma", "voice": "leda"},     # Youthful
        {"name": "Alex", "voice": "puck"}     # Upbeat
    ]
    
    text_to_speech_multi_speaker(
        casual_dialogue, 
        casual_speakers, 
        "casual_chat.wav"
    )
    print()
    
    # Example 6: Multi-speaker with style instructions
    print("Example 6: Multi-speaker with Style Control")
    styled_dialogue = get_dialogue("gemini_tts_example", "styled_dialogue")
    
    styled_speakers = [
        {"name": "Alice", "voice": "fenrir"},      # Excitable - matches excited style
        {"name": "Bob", "voice": "algieba"}       # Smooth - matches calm style
    ]
    
    text_to_speech_multi_speaker(
        styled_dialogue,
        styled_speakers,
        "styled_conversation.wav"
    )
    print()
    
    print("🎉 All examples completed! Check the generated WAV files.")
    print("\n📂 Generated files:")
    print("   • basic_example.wav - Single speaker basic TTS")
    print("   • cheerful_example.wav - Single speaker with style")
    print("   • mysterious_example.wav - Single speaker mysterious")
    print("   • tech_discussion.wav - Multi-speaker tech talk")
    print("   • casual_chat.wav - Multi-speaker casual conversation")
    print("   • styled_conversation.wav - Multi-speaker with style control")


if __name__ == "__main__":
    main() 