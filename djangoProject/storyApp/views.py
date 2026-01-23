from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# import libraries
from smolagents import CodeAgent, LiteLLMModel
from .hf_asr_whisper import transcribe_speech
from .ollama_story import create_story
from .hf_tts_mms import create_audio
from django.conf import settings

import ffmpeg

def index(request):
    return render(request, "storyApp/index.html")

def record(request):
    filename = "myPrompt.wav"
    path = settings.MEDIA_URL
    context = {"audio_file": path + filename}        
    return render(request, "storyApp/record.html", context)

@csrf_exempt
def blob(request):
    if request.method == 'POST':
        # handle uploaded file
        f = request.FILES['soundBlob']
        with open("./media/prompt_raw.wav", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        # process audio
        (
        ffmpeg
            .input('./media/prompt_raw.wav')
            .output('./media/prompt.wav',ac=1,ar=16000)
            .global_args('-y') 
            .run()
        )
        return render(request, "storyApp/record.html")

def generate(request):
    if request.method == "POST":
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
                     ./media/prompt.wav"""
        
        agent.run(prompt)
        
        context = {"feedback": "Story generated: click on 'Play a story' to hear it."}        
        
        return render(request, "storyApp/index.html", context)
    
def play(request):
    filename = "story_audio.wav"
    path = settings.MEDIA_URL
    context = {"audio_file": path + filename}        
    return render(request, "storyApp/play.html", context)