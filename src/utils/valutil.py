import os
import shutil

val_dir = "/home/anyone/Documents/sota/TurbulentWater/Water/test"

train_dir = "/home/anyone/Documents/sota/TurbulentWater/ImageNet/train"

dest_dir = "/home/anyone/Documents/sota/TurbulentWater/ImageNet/test"

for filename in os.listdir(val_dir):
    filename_parts = filename.split('_')
    subdir = os.path.join(train_dir, filename_parts[0])

    source_file = os.path.join(subdir, filename)

    dest_file = os.path.join(dest_dir, filename)
    
    shutil.copy2(source_file, dest_file)