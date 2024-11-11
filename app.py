from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

audio_file = open("data/audio.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

#store in txt file (so i dont have to read a json file)
with open("transcription.txt", "w") as file:
    file.write(transcription)