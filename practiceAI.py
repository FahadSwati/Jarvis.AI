from gtts import gTTS

text = "A beautiful sunset over the mountains with birds singing."
tts = gTTS(text)
tts.save("audio.mp3")
