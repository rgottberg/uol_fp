#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 09:50:03 2025

@author: cod
"""

# import libraries
from ollama import chat
from ollama import ChatResponse

def ollamaStory(checkpoint,user_prompt):
    response: ChatResponse = chat(model=checkpoint, 
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