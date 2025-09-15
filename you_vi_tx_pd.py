import yt_dlp
import moviepy as mp
import os
import whisper
import warnings
from fpdf import FPDF

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

def download_and_convert(url, save_path="."):
    """
    Download a YouTube video, convert it to MP3, transcribe to text, and save PDF.
    """
    try:
        # Step 1: Download video
        ydl_opts = {
            "outtmpl": f"{save_path}/%(title)s.%(ext)s"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_file = ydl.prepare_filename(info)

        print(f"Download complete: {video_file}")

        # Step 2: Convert to MP3
        mp3_file = os.path.splitext(video_file)[0] + ".mp3"
        video = mp.VideoFileClip(video_file)
        audio = video.audio
        audio.write_audiofile(mp3_file)
        audio.close()
        video.close()
        print(f"🎵 MP3 saved: {mp3_file}")

        # Step 3: Transcribe audio
        print("Generating transcript... (this may take some time)")
        model = whisper.load_model("base", device="cpu")
        result = model.transcribe(mp3_file)
        transcript_text = result["text"]

        # Step 4: Save transcript to TXT
        txt_file = os.path.splitext(video_file)[0] + ".txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(transcript_text)
        print(f"Transcript saved: {txt_file}")

        # Step 5: Save transcript to PDF
        pdf_file = os.path.splitext(video_file)[0] + ".pdf"
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        # Split transcript into lines for PDF
        for line in transcript_text.split('\n'):
            line = line.strip()
            if line:
                pdf.multi_cell(0, 8, line)
        pdf.output(pdf_file)
        print(f"PDF saved: {pdf_file}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    download_and_convert(url)
