#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 14:23:57 2026

@author: cod
"""

# import libraries
from transformers import WhisperProcessor, WhisperForConditionalGeneration, VitsModel, AutoTokenizer

# feature 1
checkpoint = "openai/whisper-medium"
checkpoint_dir = "./hf_models/whisper-medium/"

processor = WhisperProcessor.from_pretrained(checkpoint)
processor.save_pretrained(checkpoint_dir)

model = WhisperForConditionalGeneration.from_pretrained(checkpoint)
model.save_pretrained(checkpoint_dir)


# feature 3
checkpoint = "facebook/mms-tts-eng"
checkpoint_dir = "./hf_models/mms-tts-eng/"

model = VitsModel.from_pretrained(checkpoint)
model.save_pretrained(checkpoint_dir)

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
tokenizer.save_pretrained(checkpoint_dir)