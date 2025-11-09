from gtts import gTTS

def make_voice(text, path="voice.mp3", lang="en"):
    tts = gTTS(text=text, lang=lang, tld="co.in")
    tts.save(path)
    return path
