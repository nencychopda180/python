from gtts import gTTS
import os

def gujarati_text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='gu')  # 'gu' is Gujarati language code
    tts.save(filename)
    # Play the mp3 file (Windows example, change if using Mac/Linux)
    os.system(f'start {filename}')  # On Windows, or use 'afplay' on Mac

if __name__ == "__main__":
    gujarati_text = "હેલ્લો! આ ગુજરાતી ટેક્સ્ટ-ટુ-સ્પીચ ડેમો છે."
    gujarati_text_to_speech(gujarati_text)
