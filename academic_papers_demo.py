#!/usr/bin/env python3
"""
Academic Papers Multi-Speaker TTS Demo

This demo converts academic paper presentations into multi-speaker audio
using Google Gemini API. Each paper is presented by two narrators with
different voices to create engaging educational content.

Papers included:
1. GneissWeb: Preparing High Quality Data for LLMs at Scale
2. A ML-LLM Pairing for Better Code Comment Classification  
3. The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale
4. DataComp-LM: In search of the next generation of training sets for language models
5. The RefinedWeb Dataset for Falcon LLM

Usage:
    python academic_papers_demo.py
"""

import os
from gemini_tts_example import (
    text_to_speech_multi_speaker,
    create_full_paper_presentation,
)
from dialogues import get_dialogue


def demo_gneiss_web():
    """Demo: GneissWeb paper presentation."""
    print("📄 Paper 1: GneissWeb - Preparing High Quality Data for LLMs at Scale")
    
    # Using a shorter excerpt for demo purposes - you can expand this
    dialogue = get_dialogue("academic_papers_demo", "gneiss_web")
    
    speakers = [
        {"name": "Narrator 1", "voice": "kore"},     # Professional, authoritative
        {"name": "Narrator 2", "voice": "charon"}   # Informative, clear
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "gneiss_web_paper.wav")
    print()


def demo_code_comment_classification():
    """Demo: ML-LLM Code Comment Classification paper."""
    print("📄 Paper 2: A ML-LLM Pairing for Better Code Comment Classification")
    
    dialogue = get_dialogue("academic_papers_demo", "code_comment_classification")
    
    speakers = [
        {"name": "NARRATOR 1", "voice": "puck"},      # Upbeat, engaging
        {"name": "NARRATOR 2", "voice": "zephyr"}    # Bright, clear
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "code_comment_paper.wav")
    print()


def demo_fineweb_datasets():
    """Demo: FineWeb Datasets paper."""
    print("📄 Paper 3: The FineWeb Datasets - Decanting the Web for the Finest Text Data")
    
    dialogue = get_dialogue("academic_papers_demo", "fineweb_datasets")
    
    speakers = [
        {"name": "Narrator 1", "voice": "aoede"},     # Breezy, natural
        {"name": "Narrator 2", "voice": "orus"}      # Firm, knowledgeable
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "fineweb_paper.wav")
    print()


def demo_datacomp_lm():
    """Demo: DataComp-LM paper."""
    print("📄 Paper 4: DataComp-LM - In Search of the Next Generation of Training Sets")
    
    dialogue = get_dialogue("academic_papers_demo", "datacomp_lm")
    
    speakers = [
        {"name": "Narrator 1", "voice": "leda"},      # Youthful, engaging
        {"name": "Narrator 2", "voice": "fenrir"}    # Excitable, enthusiastic
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "datacomp_lm_paper.wav")
    print()


def demo_refined_web():
    """Demo: RefinedWeb Dataset paper."""
    print("📄 Paper 5: The RefinedWeb Dataset for Falcon LLM")
    
    dialogue = get_dialogue("academic_papers_demo", "refined_web")
    
    speakers = [
        {"name": "Narrator 1", "voice": "algieba"},    # Smooth, professional
        {"name": "Narrator 2", "voice": "schedar"}    # Even, balanced
    ]
    
    text_to_speech_multi_speaker(dialogue, speakers, "refined_web_paper.wav")
    print()


def main():
    """Run academic papers multi-speaker TTS demo."""
    print("🎓 Academic Papers Multi-Speaker TTS Demo")
    print("=" * 60)
    print("Converting research paper presentations to audio...")
    print()
    
    # Check if API key is available
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY environment variable not set!")
        print("Please set your API key and try again.")
        return
    
    try:
        # Run shorter demo versions of each paper
        demo_gneiss_web()
        demo_code_comment_classification()
        demo_fineweb_datasets()
        demo_datacomp_lm()
        demo_refined_web()
        
        print("🎉 Academic paper demos completed!")
        print("\n📂 Generated audio files:")
        print("   • gneiss_web_paper.wav - GneissWeb dataset research")
        print("   • code_comment_paper.wav - Code comment classification")
        print("   • fineweb_paper.wav - FineWeb datasets overview")
        print("   • datacomp_lm_paper.wav - DataComp-LM benchmark")
        print("   • refined_web_paper.wav - RefinedWeb dataset")
        
        print("\n💡 Applications for academic content:")
        print("   - Converting research papers to audio for accessibility")
        print("   - Creating podcast-style academic content")
        print("   - Generating audio summaries for literature reviews")
        print("   - Building educational audio materials")
        print("   - Making research more accessible while commuting")
        
        print("\n🔧 Customization options:")
        print("   - Adjust voice personalities for different presentation styles")
        print("   - Add emphasis and emotional tone for key findings")
        print("   - Create longer presentations with full paper content")
        print("   - Generate multiple language versions")
        
        # Offer to create full presentations
        print("\n📝 Note: This demo uses shortened excerpts.")
        print("To generate full paper presentations, use the complete scripts")
        print("provided in your input with the create_full_paper_presentation() function.")
        
    except Exception as e:
        print(f"❌ Error running academic papers demo: {e}")


if __name__ == "__main__":
    main() 