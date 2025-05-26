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


def demo_podcast_conversation():
    """Demo: Podcast conversation between a host and guest."""
    print("🎙️ Demo 1: Podcast Conversation")
    
    dialogue = """Host: Welcome to Tech Talk! I'm here with Dr. Emma Chen, an AI researcher. Emma, what's the most exciting development in AI this year?

Dr. Chen: Thanks for having me! I'd say the advancement in natural language processing is remarkable. We're seeing AI that can understand context and emotion like never before.

Host: That's fascinating! Can you give us a practical example of how this impacts everyday users?

Dr. Chen: Absolutely! Take text-to-speech technology - it's now so natural that it can convey emotions, change speaking pace, and even simulate conversations between multiple people!

Host: Amazing! Our listeners will love hearing about these developments. Where do you see this technology heading in the next few years?

Dr. Chen: I believe we'll see more personalized AI assistants that can adapt their communication style to match individual user preferences."""
    
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
    script = [
        ("Agent", "Hello! Thank you for calling TechSupport. My name is Sarah. How can I help you today?"),
        ("Customer", "Hi Sarah! I'm having trouble with my new smart speaker. It's not responding to voice commands."),
        ("Agent", "I'd be happy to help you with that! Let's start by checking if the device is properly connected to your WiFi network."),
        ("Customer", "Okay, let me check... Yes, it shows as connected to my network."),
        ("Agent", "Great! Now let's try resetting the voice recognition. Can you say 'Hey Assistant, reset voice training'?"),
        ("Customer", "Hey Assistant, reset voice training... Oh wow, it's working now! Thank you so much!"),
        ("Agent", "Wonderful! I'm glad we could resolve that quickly. Is there anything else I can help you with today?"),
        ("Customer", "No, that's perfect. Thank you for your excellent service!")
    ]
    
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
    
    dialogue = """Make the Teacher sound patient and encouraging, and the Student sound curious and engaged:

Teacher: Today we're going to learn about artificial intelligence. Can anyone tell me what AI stands for?

Student: Is it Artificial Intelligence? I think it means computers that can think like humans!

Teacher: Excellent! That's a great way to think about it. AI systems can indeed process information and make decisions, though they work differently than human brains.

Student: That's so cool! How do they learn things? Do they go to school like us?

Teacher: What a wonderful question! AI systems learn through something called machine learning, where they analyze lots of data to find patterns. It's like how you might learn to recognize different dog breeds by looking at many pictures of dogs.

Student: Oh, I get it! So the more examples they see, the better they become at recognizing things?

Teacher: Exactly right! You're really understanding this concept well. This is the same principle behind the text-to-speech technology we're using right now!"""
    
    speakers = [
        {"name": "Teacher", "voice": "charon"},     # Informative, clear
        {"name": "Student", "voice": "leda"}       # Youthful, curious
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "teacher_student_demo.wav")
    print()


def demo_story_narration():
    """Demo: Story with narrator and characters."""
    print("📚 Demo 4: Story Narration with Characters")
    
    script = [
        ("Narrator", "In a small village, two friends met at the marketplace on a busy morning."),
        ("Alice", "Good morning, Ben! I heard you've been working on something exciting."),
        ("Ben", "Alice! Yes, I've been learning about this amazing new technology called AI."),
        ("Narrator", "Alice's eyes lit up with curiosity as Ben continued."),
        ("Alice", "AI? Tell me more! I love learning about new technologies."),
        ("Ben", "Well, it can help doctors diagnose diseases, help students learn faster, and even create realistic conversations like this one!"),
        ("Narrator", "The two friends continued their conversation, both excited about the possibilities that technology could bring to their village."),
        ("Alice", "This could really help our community! We should organize a workshop to teach others."),
        ("Ben", "That's a brilliant idea! Let's start planning it right away.")
    ]
    
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
        ("Alice", "Good morning, Ben! I heard you've been working on something exciting."),
        ("Ben", "Alice! Yes, I've been learning about this amazing new technology called AI."),
        ("Alice", "AI? Tell me more! I love learning about new technologies."),
        ("Ben", "Well, it can help doctors diagnose diseases, help students learn faster, and even create realistic conversations like this one!"),
        ("Alice", "This could really help our community! We should organize a workshop to teach others."),
        ("Ben", "That's a brilliant idea! Let's start planning it right away.")
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
    
    dialogue = """Make the Interviewer sound professional and the Candidate sound confident but respectful:

Interviewer: Good morning! Please have a seat. I'm excited to learn more about your background in artificial intelligence.

Candidate: Good morning! Thank you for having me. I'm really excited about this opportunity to discuss how I can contribute to your AI research team.

Interviewer: Excellent. Can you tell me about a recent project you worked on involving machine learning?

Candidate: Certainly! I recently developed a natural language processing system that could analyze customer feedback and categorize sentiment with 95% accuracy.

Interviewer: Impressive! What challenges did you face during that project, and how did you overcome them?

Candidate: The main challenge was handling sarcasm and cultural nuances in the text. I addressed this by incorporating contextual analysis and training the model on diverse datasets from different regions.

Interviewer: That shows great problem-solving skills. How do you stay current with the rapidly evolving AI field?

Candidate: I regularly read research papers, participate in online AI communities, and work on personal projects. I actually used the Gemini API recently to explore text-to-speech capabilities!

Interviewer: Wonderful! That aligns perfectly with what we're working on here. Do you have any questions about the role or our company?"""
    
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