# uol_fp
Orchestrating AI models

# downloads
- p5.js (v1.11.11 2025-10-20) and p5.sound.js (v1.0.1 - 2021-05-25): download the complete library (https://p5js.org/download/) and save the files p5.js and p5.sound.js in the folder djangoProject/storyApp/static/storyApp/p5_library.
- HuggingFace models (ASR & TTS): run the python script "download_hf_models.py" and ensure the models are saved in the folders djangoProject/hf_models/mms-tts-eng/ and djangoProject/hf_models/whisper-medium. 
- Ollama library: download the framework with the command "curl -fsSL https://ollama.com/install.sh | sh"
- Ollama models: download the models with the commands "ollama run gemma3:1b" (LLM) and "ollama run qwen2.5-coder:3b" (agent).


# cache the tokenizer file locally.
python -c "import tiktoken; tiktoken.get_encoding('cl100k_base')"

# requirements
- run the command "pip install -r requirements.txt"

# others
- sudo apt install ffmpeg

