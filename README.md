# Introduction

This application was developed as the final project for the BSc in Computer Science of the University of London (Goldsmiths). 

The project is based on the template “4.1 Orchestrating AI models to achieve a goal” and its aim is to build a system that generates and reads stories for children, based on user prompts. 

# Installing python requirements (terminal)

- Start from the project root folder "uol_fp"
- Create virtual enviroment: python3 -m venv venv
- Run the command "pip install -r requirements.txt"

# Downloading models and other frameworks

- p5.js (v1.11.11 2025-10-20) and p5.sound.js (v1.0.1 - 2021-05-25): download the complete library (https://p5js.org/download/) and save the files p5.js and p5.sound.js in the folder djangoProject/storyApp/static/storyApp/p5_library.
- HuggingFace models (ASR & TTS): run the python script "download_hf_models.py" and ensure the models are saved in the folders djangoProject/hf_models/mms-tts-eng/ and djangoProject/hf_models/whisper-medium. 
- Ollama library: download the framework with the command "curl -fsSL https://ollama.com/install.sh | sh"
- Ollama models: download the models with the commands "ollama run gemma3:1b" (LLM) and "ollama run qwen2.5-coder:3b" (agent).
- ffmpeg: run the command sudo apt install 

# Running the app (terminal)

- Start from the project root folder "uol_fp"
- Activate the virtual environment with the command: source venv/bin/activate
- [Optional] To run the app without the internet connection, cache a "tokenizer" file locally by running the command: python -c "import tiktoken; tiktoken.get_encoding('cl100k_base')" 
- Move to the Django folder with the command cd djangoProject
- Start the server with the command python3 manage.py runserver

The app should be running on http://127.0.0.1:8000/

# Creating your story

- Start from either the "Home" page, by clicking on the button "Create a new story", or the "Create" page.
- Record your audio prompt by clicking on the button "Tell me what your story is about..."
- End your recording by clicking on the button "Stop your recording".
- [Optional] Verify your audio by clicking on the button "Play your recording".
- Start the creation process by clicking on the button "Let's generate your story". 
- Click on the button "Listen to a story" to redirect you to the audio player.

# Listening your story

- Start from the "Listen" page.
- Use the playback controls and enjoy your story.
