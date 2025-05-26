#!/usr/bin/env python3
"""
Multi-Speaker Text-to-Speech Demo using Google Gemini API

This demo showcases how to create conversations between multiple people
with different voices and speaking styles.

Usage examples:
- Podcast conversations
- Audiobook dialogues
- Educational content with teacher-student interactions
- Customer service scenarios
"""

import os
from gemini_tts_example import text_to_speech_multi_speaker, create_dialogue_from_script
from dialogues import get_dialogue


def demo_podcast_conversation():
    """Demo: Podcast conversation between a host and guest."""
    print("🎙️ Demo 1: Podcast Conversation")
    
    dialogue = get_dialogue("multi_speaker_demo", "podcast_conversation")
    
    speakers = [
        {"name": "Host", "voice": "puck"},        # Upbeat, energetic host
        {"name": "Dr. Chen", "voice": "kore"}     # Professional, authoritative
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "podcast_demo.wav")
    print()


def demo_customer_service():
    """Demo: Customer service interaction."""
    print("📞 Demo 2: Customer Service Call")
    
    # Using the script helper for cleaner code
    script = get_dialogue("multi_speaker_demo", "customer_service")
    
    dialogue = create_dialogue_from_script(script)
    
    speakers = [
        {"name": "Agent", "voice": "callirrhoe"},    # Easy-going, helpful
        {"name": "Customer", "voice": "leda"}       # Youthful, friendly
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "customer_service_demo.wav")
    print()


def demo_teacher_student():
    """Demo: Educational interaction between teacher and student."""
    print("👩‍🏫 Demo 3: Teacher-Student Interaction")
    
    dialogue = get_dialogue("multi_speaker_demo", "teacher_student")
    
    speakers = [
        {"name": "Teacher", "voice": "charon"},     # Informative, clear
        {"name": "Student", "voice": "leda"}       # Youthful, curious
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "teacher_student_demo.wav")
    print()


def demo_story_narration():
    """Demo: Story with narrator and characters."""
    print("📚 Demo 4: Story Narration with Characters")
    
    script = get_dialogue("multi_speaker_demo", "story_narration")
    
    dialogue = create_dialogue_from_script(script)
    
    speakers = [
        {"name": "Narrator", "voice": "Achird"},   # Friendly storyteller
        {"name": "Alice", "voice": "Aoede"},      # Breezy, enthusiastic
        {"name": "Ben", "voice": "Orus"}          # Firm, knowledgeable
    ]
    
    # Note: This uses 3 speakers, but Gemini supports max 2, so we'll create two versions
    print("⚠️  Note: Gemini supports max 2 speakers. Creating separate files for narrator and dialogue...")
    
    # Version 1: Just the dialogue between Alice and Ben
    dialogue_only = create_dialogue_from_script([
        line for line in script if line[0] != "Narrator"
    ])
    
    dialogue_speakers = [
        {"name": "Alice", "voice": "aoede"},      # Breezy, enthusiastic
        {"name": "Ben", "voice": "orus"}          # Firm, knowledgeable
    ]
    
    text_to_speech_multi_speaker(dialogue_only, dialogue_speakers, "story_dialogue_demo.wav")
    print()


def demo_interview():
    """Demo: Job interview scenario."""
    print("💼 Demo 5: Job Interview")
    
    dialogue = get_dialogue("multi_speaker_demo", "interview")
    
    speakers = [
        {"name": "Interviewer", "voice": "kore"},     # Professional, firm
        {"name": "Candidate", "voice": "zephyr"}     # Bright, confident
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "interview_demo.wav")
    print()


def main():
    """Run all multi-speaker demos."""
    print("🎭 Multi-Speaker Text-to-Speech Demos")
    print("=" * 50)
    print()
    
    # Check if API key is available
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY environment variable not set!")
        print("Please set your API key and try again.")
        return
    
    try:
        demo_podcast_conversation()
        demo_customer_service()
        demo_teacher_student()
        demo_story_narration()
        demo_interview()
        
        print("🎉 All multi-speaker demos completed!")
        print("\n📂 Generated files:")
        print("   • podcast_demo.wav - Tech podcast conversation")
        print("   • customer_service_demo.wav - Support call simulation")
        print("   • teacher_student_demo.wav - Educational interaction")
        print("   • story_dialogue_demo.wav - Story character dialogue")
        print("   • interview_demo.wav - Job interview scenario")
        print("\n💡 Tip: You can use these patterns for:")
        print("   - Creating audiobooks with character voices")
        print("   - Generating training materials for customer service")
        print("   - Building educational content with interactive dialogues")
        print("   - Producing podcast-style content automatically")
        
    except Exception as e:
        print(f"❌ Error running demos: {e}")


if __name__ == "__main__":
    main() 