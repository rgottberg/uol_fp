# import libraries
from smolagents import tool
from ollama import chat
from ollama import ChatResponse

@tool
def create_story(user_prompt: str) -> str:
    """
    This is a tool that creates and returns stories for children. This tool 
    must receive exactly 1 argument, which is the user prompt.
    It returns a newly-created story.

    Args:
        user_prompt: information provided by users to create a story.
    """
    # checkpoint name
    checkpoint = "granite3.1-moe:1b"
    # inference
    response: ChatResponse = chat(model=checkpoint,
                                  messages=[
                                      {
                                          'role': 'system',
                                          'content': """write a story 
                                          for children based on user prompt and 
                                          ensure that:
                                          - word limit is 100 words;
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
    # return story text
    return response["message"]["content"]