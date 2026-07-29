from RealtimeTTS import TextToAudioStream, SystemEngine

engine = SystemEngine()
stream = TextToAudioStream(engine)

text = "Hello Mona, your voice assistant is working successfully."

print("Speaking...")

stream.feed(text)
stream.play()

print("Done!")

