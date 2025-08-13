
from moviepy.editor import VideoFileClip
import os

# Get absolute path to avoid OneDrive issues
base_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(base_dir, "WhatsApp Video_22.mp4")
audio_path = os.path.join(base_dir, "audio_extracted.mp3")

# Load video
video = VideoFileClip(video_path)

# Extract audio if available
if video.audio:
    video.audio.write_audiofile(audio_path)
    print(f" Audio extracted and saved as: {audio_path}")
else:
    print(" This video has no audio track.")

video.close()
