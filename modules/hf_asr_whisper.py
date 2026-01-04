#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 17:52:36 2025

@author: cod
"""

# import libraries
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio
import torch

def hfWhisper(file_path):
    checkpoint = "openai/whisper-medium"
    
    processor = WhisperProcessor.from_pretrained(checkpoint)
    model = WhisperForConditionalGeneration.from_pretrained(checkpoint)
    
    model.config.forced_decoder_ids = None
    
    waveform, sample_rate = torchaudio.load(file_path)
    
    input_features = processor(waveform.squeeze().numpy(), sampling_rate=16000, return_tensors="pt").input_features
    
    with torch.no_grad():
        predicted_ids = model.generate(input_features)
        transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    
    return transcription[0]