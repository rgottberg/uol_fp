#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 09:43:12 2025

@author: cod
"""

# import libraries
from shiny import App, render, ui,reactive
from modules import ollama_story, hf_tts_mms,hf_asr_whisper 
from pathlib import Path
import torchaudio

# UI
app_ui = ui.page_fluid(
    ui.navset_card_pill(
        ui.nav_panel(
            "Prototype",
            ui.layout_column_wrap(
                ui.card(
                    ui.card_header(ui.h3("Project scope & workflow")),
                    ui.output_image("image1"),
                    ),
                ui.card(
                    ui.card(
                        ui.card_header(ui.h4("1. automatic speech recognition")),
                        ui.input_file("input_file", 
                                      "Select a file"),
                        ui.output_text("txt_out_1")
                        ),
                    ui.card(
                        ui.card_header(ui.h4("2. text generation")),
                        ui.input_text(
                            "txt_in", 
                            "Your story is about ...",
                            "",
                            update_on = "blur"),
                        ui.output_text("txt_out_2")
                        ),
                    ui.card(
                        ui.card_header(ui.h4("3. speech synthesis")),
                        ui.input_task_button("audio",
                                             "Generate audio",
                                             label_busy='Generating...')
                        ),
                    ),
                ),
            ),
        ),
    theme=Path(__file__).parent / "modules" / "my_theme.css"
    )

# Server
def server(input, output, session):
        
    @render.image  
    def image1():
        img = {"src": "./images/20251103_workflow.png", "width": "100%"}  
        return img

    @reactive.calc
    def transcription():
        file = input.input_file()
        if file:
            user_request = hf_asr_whisper.hfWhisper(file[0]["datapath"])
            return user_request

    @render.text
    def txt_out_1():
        return transcription() 

    @reactive.calc
    def generate_text():
        checkpoint = "gemma3:1b" #chosen model
        # checkpoint = "granite3.1-moe:3b" #chosen model
        story = ""
        if input.txt_in():
            story,response = ollama_story.ollamaStory(checkpoint,input.txt_in())
        return story
   
    @render.text
    def txt_out_2():
        return generate_text()
    
    @reactive.calc
    def generate_audio():
        story = generate_text()
        output,sampling_rate = hf_tts_mms.hfMMS(story)
        torchaudio.save("./story_audio.wav", output.squeeze(0), sampling_rate)
        
    @reactive.effect
    @reactive.event(input.audio)
    def download_audio():
        if input.txt_in():
            generate_audio()

# Shiny app
app = App(app_ui, server)
