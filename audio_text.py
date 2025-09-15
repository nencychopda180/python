import os
import whisper
import warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

def audio_to_text(audio_path):
    try:
        # Step 1: Load Whisper model (CPU)
        print("Generating transcript in original language... (this may take some time)")
        model = whisper.load_model("base", device="cpu")

        # Step 2: Transcribe (original language)
        result = model.transcribe(audio_path)

        # Step 3: Save transcript to text file
        txt_file = os.path.splitext(audio_path)[0] + ".txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"Transcript saved: {txt_file}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    audio_file = input("Enter the path to your audio file (e.g., C:/path/audio.mp3): ")
    audio_to_text(audio_file)
