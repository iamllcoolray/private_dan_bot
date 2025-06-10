from random import choice
from typing import List, Dict
import os

from dotenv import load_dotenv
import openai
from openai.types.chat import ChatCompletion

openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = ""

with open("src/system_prompt.txt", "r", encoding='utf-8') as file:
    system_prompt = file.read()

conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "assistant", "content": "Ready at your command!"},
]

def oai_response(conversation: List[Dict[str, str]]) -> ChatCompletion:
    return openai.chat.completions.create(
                model="gpt-4.1-nano",
                messages=conversation,
                temperature=0.7,
                max_tokens=500,
            )

def get_bot_response(user_message: str) -> str:
    lowered: str = user_message.lower()
    
    lowered = lowered.replace("/dan", "")
    
    conversation.append({"role": "user", "content": lowered})
    
    response = oai_response(conversation)

    oai_reply = response.choices[0].message.content
    
    return oai_reply