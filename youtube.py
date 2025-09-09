from pytube import YouTube
import os

def download_youtube_video(url, output_path="."):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution video stream
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # Download the video
        print(f"Downloading: {yt.title}")
        video.download(output_path)
        print(f"Download completed! Video saved to {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example URL
    video_url = "https://www.youtube.com/watch?v=xV9HnITo2C0"
    # Specify output directory (current directory by default)
    output_directory = "."
    
    download_youtube_video(video_url, output_directory)