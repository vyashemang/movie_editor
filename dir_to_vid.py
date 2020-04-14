import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS, BASE_DIR
from moviepy.editor import ImageSequenceClip
from PIL import Image

#source_file_name = input("Enter the folder path: ") 
#output_folder_name = input("Enter the output folder path: ") 
#file_path = os.path.join(BASE_DIR, str(source_file_name))
#output_folder_path = os.path.join(BASE_DIR, str(output_folder_name))
#source_clip = os.path.join(SAMPLE_INPUTS, "output.mp4")

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
output_video = os.path.join(SAMPLE_OUTPUTS, 'final_div_to_vid.mp4')

this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("jpg")]

directory = {}
for root, dirs, files in os.walk(thumbnail_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_path = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_path.append(filepath)

clip = ImageSequenceClip(new_path, fps=5)
clip.write_videofile(output_video)
