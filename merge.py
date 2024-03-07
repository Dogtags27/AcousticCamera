# import ffmpeg

# # Input files
# video_input = 'video.avi'
# audio_input = 'audio.wav'

# # Output file
# output_file = 'output.mp4'

# # Build FFmpeg command
# ffmpeg.input(video_input).input(audio_input).output(output_file, vcodec='copy', acodec='aac').run()
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# Directory paths
current_directory = os.path.dirname(os.path.abspath(__file__))
records_directory = os.path.join(current_directory,'recorder_output', 'records')

# Input files
video_input = os.path.join(records_directory, 'video.avi')
audio_input = os.path.join(records_directory, 'audio.wav')
# print(video_input)
# Output file
output_file = os.path.join(records_directory, 'output.mp4')
print(audio_input)
# Load video and audio clips
video_clip = VideoFileClip(video_input)
audio_clip = AudioFileClip(audio_input)

# Set audio for video clip
video_clip = video_clip.set_audio(audio_clip)

# Write merged video with audio to output file
video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
