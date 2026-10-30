from openrouter import OpenRouter
from dotenv import load_dotenv
import os

load_dotenv()

# model 1
with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
    response = client.chat.send(
        model="nvidia/nemotron-3.5-lightning:free",
        messages=[
            {"role": "user", "content": "What is the easiest coding language?"}
        ],
    )

print(response.choices[0].message.content)


# model 2
with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
    response = client.chat.send(
        model="dots-studio/dots-3-note-preview:free",
        messages=[
            {"role": "user", "content": "What is the hardest coding language?"}
        ],
    )

print(response.choices[0].message.content)