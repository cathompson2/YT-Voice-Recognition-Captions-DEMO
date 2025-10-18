import whisper

model = whisper.load_model('base')
result = model.transcribe('how to make pickle  pepsi at home  for free.mp3')
print(result['text'])