#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 09:43:12 2025

@author: cod
"""

# import libraries
from shiny import App, render, ui,reactive
from pathlib import Path

import sys
sys.path.insert(0, "./modules")

from smolagents import CodeAgent, LiteLLMModel
from hf_asr_whisper import transcribe_speech
from ollama_story import create_story
from hf_tts_mms import create_audio


# UI
app_ui = ui.page_fluid(
    ui.navset_card_pill(
        ui.nav_panel(
            "Prototype",
            ui.card(
                ui.card_header(ui.h4("Generate your own story")),
                ui.input_task_button("story",
                                     "Generate",
                                     label_busy='Generating ...')
                ),
            ),
        ),
    theme=Path(__file__).parent / "modules" / "my_theme.css"
    )

# Server
def server(input, output, session):
    
    model = LiteLLMModel(
        model_id="ollama_chat/qwen2.5-coder:3b",
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
                         
    @reactive.calc
    def generate_story():
        agent.run(prompt)
        
    @reactive.effect
    @reactive.event(input.story)
    def download_story():
        generate_story()

# Shiny app
app = App(app_ui, server)
