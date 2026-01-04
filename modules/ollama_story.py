#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 09:50:03 2025

@author: cod
"""

from ollama import chat
from ollama import ChatResponse
import pandas as pd
import re

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

    df = pd.DataFrame.from_dict(response)
    df = df.T
    column_labels = df.loc[0]
    df = df.rename(columns=column_labels)
    df = df.rename({"model":"checkpoint"},axis=1)
    df = df.drop(0)
    df = df.reset_index(drop=True)
    df["prompt"] = user_prompt
    df["story"] = df["message"].apply(lambda x: x["content"])
    
    #story = re.split(r'\s+', story)
    #story = " ".join(story)
    df["story_tokens"] = df["story"].apply(lambda x: len(re.split(r'\s+',x)))

    df["time_per_output_token"] = df["total_duration"]/df["story_tokens"]
    story = df.loc[0,"story"]
    return story,df