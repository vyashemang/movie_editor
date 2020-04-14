from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS, BASE_DIR
from moviepy.editor import VideoFileClip
from PIL import Image

source_file_name = input("Enter the video file path(.mp4): ") 
output_folder_name = input("Enter the output folder path: ") 

#file_path = os.path.join(BASE_DIR, str(source_file_name))
#output_folder_path = os.path.join(BASE_DIR, str(output_folder_name))
#source_clip = os.path.join(SAMPLE_INPUTS, "output.mp4")

thumbnail_dir = os.path.join(output_folder_name, "thumbnails")

if not os.path.exists(thumbnail_dir):
    os.makedirs(thumbnail_dir)

clip = VideoFileClip(source_file_name)
print("No of frames in this video clip is: " + str(clip.reader.nframes))
print("Total duration of this clip is: " + str(clip.duration))

duration = clip.duration
max_duration = int(duration) + 1

for i in range(0, max_duration):
    frame = clip.get_frame(i)
    new_img_filepath = os.path.join(thumbnail_dir, str(i)+".jpg")
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)

print("Thumbnails created check out in output folder!")