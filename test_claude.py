import os
from anthropic import Anthropic

# set key manually:
# export ANTHROPIC_API_KEY='your-api-key-here'
# client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# get key from .env instead:
from dotenv import load_dotenv
load_dotenv()
client = Anthropic()


message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude! What is the distance from Earth to Moon?"}
    ]
)

print(message.content[0].text)