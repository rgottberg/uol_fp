# import libraries
from smolagents import tool
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio
import torch

@tool
def transcribe_speech(file_path: str) -> str:
    """
    This is a tool that converts speech into text. This tool must receive 
    exactly 1 argument, which is the path to the file containing the speech. 
    It returns a speech transcription.

    Args:
        file_path: path to the file containing the speech.
    """
    # folder containing checkpoint
    checkpoint_dir = "./hf_models/whisper-medium/"
    # load processor from local files
    processor = WhisperProcessor.from_pretrained(checkpoint_dir,
                                                 local_files_only=True)
    # load model from local files
    model = WhisperForConditionalGeneration.from_pretrained(checkpoint_dir,
                                                            local_files_only=True)
    # configuration
    model.config.forced_decoder_ids = None
    # load audio file
    waveform, sample_rate = torchaudio.load(file_path)
    # preprocess audio
    input_features = processor(waveform.squeeze().numpy(), 
                               sampling_rate=16000, 
                               return_tensors="pt").input_features
    # inference
    with torch.no_grad():
        predicted_ids = model.generate(input_features)
        transcription = processor.batch_decode(predicted_ids, 
                                               skip_special_tokens=True)
    # return audio transcription
    return transcription[0]