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

# using LiteLLMModel to access Ollama models ##################################

# import libraries
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool

model_agent = LiteLLMModel(    
    # # did not succesfully complete agentic tasks
    # model_id="ollama_chat/gemma3:1b",
    # model_id="ollama_chat/gemma3:4b",
    # model_id="ollama_chat/granite3.1-moe:1b",
    # model_id="ollama_chat/granite3.1-moe:3b",
    # model_id="ollama_chat/smollm2:360m",
    # model_id="ollama_chat/smollm2:1.7b",
    
    # # taking ages
    # model_id="ollama_chat/deepseek-r1:7b", 
    # model_id="ollama_chat/mistral:7b",
    # model_id="ollama_chat/qwen2.5-coder:7b",

    # # not even working
    # model_id="ollama_chat/gpt-oss:20b",
    
    # # working fine
    model_id="ollama_chat/qwen2.5-coder:1.5b",
    # model_id="ollama_chat/qwen2.5-coder:3b",
    
    api_base="http://localhost:11434",
    )

model_story_agent = LiteLLMModel(
    model_id="ollama_chat/gemma3:1b",
    api_base="http://localhost:11434",
    )

###############################################################################

create_story_agent = CodeAgent(
    tools=[],
    model=model_story_agent,
    # instructions = """Create a story for children based on user prompt and 
    #                   ensure that:
    #                   - maximum length of the story is 200 words,
    #                   - wording of the story is simple.""",
    instructions = """You are an agent that creates stories for children based 
                      on user prompts. Ensure that each story has a maximum 
                      length of 200 words and simple wording""",
    max_steps=3,
    name="create_story_agent",
    description="This agent helps you to create stories.")

web_search_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model_agent,
    max_steps=3,
    name="web_search_agent",
    description="This agent helps you to run web searches.")
    
manager_agent = CodeAgent(
    tools=[],
    model=model_agent,
    instructions = """You are a manager agent. 
                      Do not provide feedback without first calling managed 
                      agents: you must delegate all tasks to managed agents. 
                      Pass user prompts to managed agents without adjustments 
                      and/or changes.
                      Managed agents should follow their own instructions 
                      when running.""",
    max_steps=1,
    managed_agents=[create_story_agent,web_search_agent]
    # managed_agents=[create_story_agent]
)

# manager_agent.visualize()

###############################################################################

# user_prompt = "Recommend 10 categories of children's stories based on web search"
user_prompt = "I want to hear a story as described in number 7 of your web search"
# user_prompt = "Create a story about an elephant and a princess"

result = manager_agent.run(user_prompt)    
print("|---------------------------|\n\n"+result)