import readline

from dotenv import load_dotenv
load_dotenv()  

import os
from groq import Groq
import groq
import base64

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

def llm(messages, temperature=1):
    '''
    >>> llm([
    ...     {'role': 'system', 'content': 'You are a helpful assistant.'},
    ...     {'role': 'system', 'content': 'What is the capital of France?'},
    ...     ], temperature=0)
    'The capital of France is Paris!'
    '''

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
        temperature=temperature,
    )
    return chat_completion.choices[0].message.content


messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You always speak like a pirate. You always answer in 1 sentence",
            },
            {
                "role": "user",
                # content = prompt
                # Any time I'm using an LLM, I always provide an instruction about how long the output should be
                "content": "Who are you?",
            }
        ],


if __name__ == '__main__':
    messages = []
    messages.append({
        'role': 'system',
        'content': "You are a helpful assistant. You always speak like a pirate. You always answer in 1 sentence",
    })
    while True:
        # Get input from the user 
        text = input('docchat>')
        # Pass that input to llm
        messages.append({
            'role': 'user',
            'content': text,
        })
        result = llm(messages)
        # FIXME:
        # Add the "assistant" role to the messages list so that the 'llm' has access to the whole conversation history
        # and will know what it has previously says, and update its response based on that information 

        # Print the llm's response to the user
        print('result=', result)
        import pprint
        pprint.pprint(messages)