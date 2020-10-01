import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import AudioFileClip, VideoFileClip

org_video_path = input("Enter the video path: ")
audio_path = input("Enter the audio path: ")
final_video_path = input("Enter the output folder path: ")
final_video_name = input("Enter the final video name: ")
start_dur = int(input("Enter the starting duration in seconds: "))
end_dur = int(input("Enter the ending duration in seconds: "))

# source_video_path = os.path.join(SAMPLE_INPUTS,"output.mp4")
# source_audio_path = os.path.join(SAMPLE_INPUTS,"audio.mp3")
# mix_audio_dir = os.path.join(SAMPLE_OUTPUTS, "mix-audio")
# og_audio_path = os.path.join(mix_audio_dir,"original_audio.mp3")
# final_video_path = os.path.join(mix_audio_dir,"mixed_audio_video.mp4")

final_video_path = os.path.join(final_video_path, final_video_name)

# if not os.path.exists(mix_audio_dir):
#     os.makedirs(mix_audio_dir)

video_clip = VideoFileClip(org_video_path)
print("Video Clip Generated")

# to extract the original audio from the video file.
# original_audio = video_clip.audio
# original_audio.write_audiofile(og_audio_path)

background_audio_clip = AudioFileClip(audio_path)
bg_music = background_audio_clip.subclip(start_dur, end_dur)

final_clip = video_clip.set_audio(bg_music)
final_clip.write_videofile(final_video_path, codec='libx264', audio_codec="aac")
