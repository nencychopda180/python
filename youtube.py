import yt_dlp

def download_video(url, save_path="."):
    ydl_opts = {
        "outtmpl": f"{save_path}/%(title)s.%(ext)s"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    download_video(url)