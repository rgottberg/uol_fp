#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 10:47:33 2026

@author: cod
"""

# using LiteLLMModel to access Ollama models ##################################

# import libraries
from smolagents import CodeAgent, LiteLLMModel
from hf_asr_whisper import transcribe_speech
from ollama_story import create_story
from hf_tts_mms import create_audio

model = LiteLLMModel(
    # # did not succesfully complete agentic tasks
    # model_id="ollama_chat/gemma3:1b",
    # model_id="ollama_chat/gemma3:4b",
    # model_id="ollama_chat/granite3.1-moe:1b",
    # model_id="ollama_chat/granite3.1-moe:3b",
    # model_id="ollama_chat/smollm2:360m",
    # model_id="ollama_chat/smollm2:1.7b",
    
    # # taking ages
    # model_id="ollama_chat/deepseek-r1:7b", 
    # model_id="ollama_chat/mistral:7b",
    # model_id="ollama_chat/qwen2.5-coder:7b",

    # # not even working
    # model_id="ollama_chat/gpt-oss:20b",
    
    # # working fine
    # model_id="ollama_chat/qwen2.5-coder:1.5b",
    model_id="ollama_chat/qwen2.5-coder:3b",
    api_base="http://localhost:11434",
    )
   
agent = CodeAgent(
    tools=[transcribe_speech,create_story,create_audio],
    model=model,
    max_steps=3
)

prompt = """ Create an audio story for children based on the user prompt 
             contained in the audio file stored at the following path 
             ../data/input_asr/1_audio_man.wav"""
                 

result = agent.run(prompt)    
print("|---------------------------|\n\n"+result)