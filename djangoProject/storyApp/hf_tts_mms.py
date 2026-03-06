# import libraries
from smolagents import tool
from transformers import VitsModel, AutoTokenizer
import torch
import torchaudio
from pathlib import Path
from django.conf import settings

@tool
def create_audio(story: str, file_path: str) -> str:
    """
    This is a tool that converts text into speech. This tool must receive 
    exactly 2 arguments, which is the text of the story the path to the output 
    file. 
    It returns an audio file labelled "story_audio.wav".

    Args:
        story: text of the story to be converted into speech.
        file_path: path to the output audio file.
    """
    # folder containing checkpoint
    checkpoint_dir = "./hf_models/mms-tts-eng/"
    # load model from local files
    model = VitsModel.from_pretrained(checkpoint_dir,
                                      local_files_only=True)
    # load tokenizer from local files
    tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir,
                                              local_files_only=True)
    # tokenize text
    inputs = tokenizer(story, return_tensors="pt")
    # inference
    with torch.no_grad():
        output = model(**inputs).waveform
    # save audio file
    filename = "story_audio.wav"
    file_path = Path(settings.MEDIA_ROOT)
    torchaudio.save(file_path / filename,
                    output.squeeze(0), 
                    model.config.sampling_rate)
    # return name of audio file
    return "story_audio.wav"