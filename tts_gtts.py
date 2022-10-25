from fastapi import FastAPI
from gtts import gTTS
from IPython.display import Audio
import base64 


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!!"}


@app.post("/text_to_speech")
def gtts(text, lang):
  tts = gTTS(text,lang =f'{lang}')
  tts.save('1.wav')
  sound_file = '1.wav'
  file = open("1.wav", 'rb').read()
  enc=base64.b64encode(file)
  return enc

# print(gtts("this is a good book",'en'))

