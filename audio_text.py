import speech_recognition as sr
from pydub import AudioSegment

# Convert mp3 to wav
sound = AudioSegment.from_mp3(r"C:\\Users\\nency\\Documents\\tmkoc.mp3.mp3")
sound.export("audio.wav", format="wav")

# Speech recognition
recognizer = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language="en-IN")
    print("Transcript:", text)
