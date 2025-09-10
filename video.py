import moviepy.editor as mp
import os

def convert_video_to_mp3(video_path, output_path=None):
    """
    Convert a video file to MP3 audio format.
    
    Args:
        video_path (str): Path to the input video file
        output_path (str, optional): Path to save the output MP3 file
    """
    try:
        # If no output path is specified, create one from the input file name
        if output_path is None:
            output_path = os.path.splitext(video_path)[0] + '.mp3'
        
        # Load the video file
        video = mp.VideoFileClip(video_path)
        
        # Extract the audio
        audio = video.audio
        
        # Save the audio as MP3
        audio.write_audiofile(output_path)
        
        # Clean up
        audio.close()
        video.close()
        
        print(f"Successfully converted {video_path} to {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    video_file = input("Enter the path to your video file: ")
    convert_video_to_mp3(video_file)