#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 22:13:34 2025

@author: cod
"""

# import libraries
from smolagents import tool
from transformers import VitsModel, AutoTokenizer
import torch
import torchaudio
from pathlib import Path
from django.conf import settings

@tool
def create_audio(story: str) -> str:
    """
    This is a tool that converts text into speech. This tool must receive 
    exactly 1 argument, which is the text of the story. 
    It returns an audio file labelled "story_audio.wav".

    Args:
        story: text of the story to be converted into speech.
    """
    checkpoint_dir = "./hf_mms-tts-eng/"
    model = VitsModel.from_pretrained(checkpoint_dir)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir)
        
    inputs = tokenizer(story, return_tensors="pt")
    
    with torch.no_grad():
        output = model(**inputs).waveform

    filename = "story_audio.wav"
    path = Path(settings.MEDIA_ROOT)

    torchaudio.save(path / filename,
                    output.squeeze(0), 
                    model.config.sampling_rate)
    
    return "story_audio.wav"