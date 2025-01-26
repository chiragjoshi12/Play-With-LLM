from pathlib import Path
from openai import OpenAI

# Create client using OPENAI_API_KEY
client = OpenAI(api_key="OPENAI_API_KEY") # Replace "OPENAI_API_KEY" with your API

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something. making humanity"
)

response.stream_to_file(speech_file_path)