from openai import OpenAI

# Create client using OPENAI_API_KEY
client = OpenAI(api_key="OPENAI_API_KEY") # Replace "OPENAI_API_KEY" with your API

audio_file= open("./Data/speech.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcription.text)