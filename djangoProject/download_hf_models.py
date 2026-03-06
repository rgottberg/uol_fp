# import libraries
from transformers import WhisperForConditionalGeneration, WhisperProcessor, VitsModel, AutoTokenizer, AutoModelForCausalLM

# ASR
## checkpoint name
checkpoint = "openai/whisper-medium"
## destination folder
checkpoint_dir = "./hf_models/whisper-medium/"
## load (& save copy in HF folder)
model = WhisperForConditionalGeneration.from_pretrained(checkpoint)
processor = WhisperProcessor.from_pretrained(checkpoint)
## save copy in destination folder
model.save_pretrained(checkpoint_dir)
processor.save_pretrained(checkpoint_dir)

# TTS
## checkpoint name
checkpoint = "facebook/mms-tts-eng"
## destination folder
checkpoint_dir = "./hf_models/mms-tts-eng/"
## load (& save copy in HF folder)
model = VitsModel.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
## save copy in destination folder
model.save_pretrained(checkpoint_dir)
tokenizer.save_pretrained(checkpoint_dir)