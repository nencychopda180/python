import whisper
import warnings

# Ignore FP16 warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

def transcribe_audio(audio_path, output_file="transcript.txt"):
    try:
        print("Loading Whisper model...")
        model = whisper.load_model("base")

        print(f"Transcribing: {audio_path}")
        result = model.transcribe(audio_path)

        transcript = result["text"]

        print("\n--- Transcript ---\n")
        print(transcript)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript)

        print(f"\nTranscript saved to: {output_file}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    audio_path = input("Enter the path to your audio file (.mp3/.wav): ").strip('"')
    transcribe_audio(audio_path)