from django.shortcuts import render
from django.conf import settings

# import libraries
from smolagents import LiteLLMModel, CodeAgent
from .hf_asr_whisper import transcribe_speech
from .ollama_story import create_story
from .hf_tts_mms import create_audio
import ffmpeg

# home
def index(request):
    return render(request, "storyApp/index.html")

# recorder
def record(request):
    filename = "myPrompt.wav"
    path = settings.MEDIA_URL
    context = {"audio_file": path + filename}
    return render(request, "storyApp/record.html", context)

# process audio received from frontend
def blob(request):
    if request.method == 'POST':
        # handle uploaded file
        f = request.FILES['soundBlob']
        with open("./media/prompt_raw.wav", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        # convert to format required by ASR
        (
        ffmpeg
            .input('./media/prompt_raw.wav')
            .output('./media/prompt.wav',ac=1,ar=16000)
            .global_args('-y') 
            .run()
        )
        return render(request, "storyApp/record.html")

# AI orchestration
def generate(request): 
    if request.method == "POST":
        # initialize model
        model = LiteLLMModel(
            model_id="ollama_chat/qwen2.5-coder:3b",
            temperature=0.0,
            api_base="http://localhost:11434"
            )
        # initialize agent
        agent = CodeAgent(
            tools=[transcribe_speech,create_story,create_audio],
            model=model,
            max_steps=3
        )
        # agent instructions
        prompt = """ 
        Create an audio story for children based on the user prompt contained 
        in the audio file stored at the following path: ./media/prompt.wav 
        """
        # inference
        agent.run(prompt)
        # return feedback to user
        context = {"feedback": "You can now play your story."}
        return render(request, "storyApp/index.html", context)

# audio player
def play(request):
    filename = "story_audio.wav"
    path = settings.MEDIA_URL
    context = {"audio_file": path + filename}        
    return render(request, "storyApp/play.html", context)
