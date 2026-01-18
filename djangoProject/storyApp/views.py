from django.shortcuts import render

# import libraries
from smolagents import CodeAgent, LiteLLMModel
from .hf_asr_whisper import transcribe_speech
from .ollama_story import create_story
from .hf_tts_mms import create_audio


def index(request):
    model = LiteLLMModel(
        model_id="ollama_chat/qwen2.5-coder:3b",
        # model_id="ollama_chat/llama3.2:3b",
        api_base="http://localhost:11434",
        )
       
    agent = CodeAgent(
        tools=[transcribe_speech,create_story,create_audio],
        model=model,
        max_steps=3
    )

    prompt = """ Create an audio story for children based on the user prompt 
                 contained in the audio file stored at the following path: 
                 ./3_audio_man.wav"""
        
    agent.run(prompt)
    return render(request, "storyApp/index.html")