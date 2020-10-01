import os
import pandas
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image

org_video_path = input("Enter the video path: ")
final_video_path = input("Enter the output folder path: ")
final_video_name = input("Enter the final video name: ")
audio_path = input("Enter the final video name: ")
watermark = input("Enter the watermark: ")

final_video_path = os.path.join(final_video_path, final_video_name)

video_clip = VideoFileClip(org_video_path)
audio_clip = AudioFileClip(audio_path)
final_audio = audio_clip.subclip(25, 40)

w, h = video_clip.size
fps = video_clip.fps

intro_duration = 5
intro_text = TextClip("Hello world!", fontsize=70, color='white', size=video_clip.size)
intro_text = intro_text.set_duration(intro_duration)
intro_text = intro_text.set_fps(fps)
intro_text = intro_text.set_pos("center")

# to add audio to your intro:

intro_music = audio_clip.subclip(25, 30)
intro_text = intro_text.set_audio(intro_music)

watermark_size = 50
watermark_text = TextClip(watermark, fontsize=watermark_size, color='black', align='East', size=(w, watermark_size))
watermark_text = watermark_text.set_fps(fps)
watermark_text = watermark_text.set_duration(video_clip.reader.duration)
watermark_text = watermark_text.margin(left=10, right=10, bottom=2, opacity=0)
watermark_text = watermark_text.set_position(("bottom"))

watermarked_clip = CompositeVideoClip([video_clip, watermark_text], size=video_clip.size)
watermarked_clip = watermarked_clip.set_duration(video_clip.reader.duration)
watermarked_clip = watermarked_clip.set_fps(fps)
watermarked_clip = watermarked_clip.set_audio(final_audio)

final_clip = concatenate_videoclips([intro_text, watermarked_clip])
final_clip.write_videofile(final_video_path, codec='libx264', audio_codec="aac")
