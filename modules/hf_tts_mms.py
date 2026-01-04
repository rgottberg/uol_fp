#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 22:13:34 2025

@author: cod
"""

# import libraries
from transformers import VitsModel, AutoTokenizer
import torch

def hfMMS(story):
    checkpoint_dir = "./hf_mms-tts-eng/"
    model = VitsModel.from_pretrained(checkpoint_dir)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir)
        
    inputs = tokenizer(story, return_tensors="pt")
    
    with torch.no_grad():
        output = model(**inputs).waveform
    
    return output, model.config.sampling_rate 
