#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:17:23 2026

@author: cod
"""

# # using TransformersModel to access HF models ###############################

# # import libraries
# from smolagents import CodeAgent, TransformersModel, DuckDuckGoSearchTool

# model = TransformersModel(
#     # model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
#     # model_id="HuggingFaceTB/SmolLM2-360M-Instruct",
#     model_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",
#     )

# using LiteLLMModel to access Ollama models ################################

# import libraries
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool

model = LiteLLMModel(
    # model_id="ollama_chat/gemma3:1b",
    # model_id="ollama_chat/gpt-oss:20b",
    # model_id="ollama_chat/smollm2:360m",
    model_id="ollama_chat/smollm2:1.7b",
    api_base="http://localhost:11434",
    )

###############################################################################

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    add_base_tools=True)

result = agent.run("Search for current weather in Luxembourg.")
print(result)