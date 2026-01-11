#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 09:50:03 2025

@author: cod
"""

# import libraries
from smolagents import tool
from ollama import chat
from ollama import ChatResponse

@tool
def createStory(user_prompt: str) -> str:
    """
    This is a tool that creates and returns stories for children based on user 
    prompts. This tool must receive exactly 1 argument, which is the user prompt. 
    This tool returns a newly-created story.

    Args:
        user_prompt: information provided by users to create a story.
    """
    response: ChatResponse = chat(model="gemma3:1b",
                                  messages=[
                                      {
                                          'role': 'system',
                                          'content': """write a story 
                                          for children based on user prompt and 
                                          ensure that:
                                          - word limit is 200 words;
                                          - the wording is simple (use simple 
                                                                   words and 
                                                                   avoid using
                                                                   too many 
                                                                   adjectives 
                                                                   and/or adverbs);
                                          - in the content of the reponse, 
                                          there is no interaction with the user
                                          (do not provide details of the prompt 
                                           and/or ask questions to the user)"""
                                          },
                                      {
                                          'role': 'user',
                                          'content': user_prompt
                                          },
                                      ]
                                  )

    story = response["message"]["content"]
    return story