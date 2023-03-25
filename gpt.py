#!/usr/bin/env python3
#Import open AI OS and System Modules
import openai,os,sys
from dotenv import load_dotenv

load_dotenv()

# accessing parsed_text
with open('resume_text.txt') as f:
    resume_text = f.read()

openai.api_key = os.getenv('CHAT_GPT_API_KEY')
messages = [
        {"role": "system", "content": "You are a helpful assistant."},
]
while True:
    message = "summarize this text for resume with proper indentation"+resume_text
    if message:
        messages.append(
                {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
        )
    print("Summarizing the text...")
    answer = chat_completion.choices[0].message.content
    resume_text=answer
    f = open("summary.txt", "w")
    f.write(resume_text)
    f.close()
    print("----------------------------------"+"The summarized text is:"+"----------------------------------")
    print(resume_text)
    break

# for getting prompt for images
while True:
    message = "get the prompt keywords for stable diffusion for the given text"+ "'" + resume_text + "'"
    if message:
        messages.append(
                {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
        )
    print("Getting the prompt keywords...")
    answer = chat_completion.choices[0].message.content
    f = open("prompt_text.txt", "w")
    f.write(answer)
    f.close()
    print("----------------------------------"+"The prompt keywords are:"+"----------------------------------")
    print(answer)
    break