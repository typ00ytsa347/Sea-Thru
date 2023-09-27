import os
import shutil

src_dir = "/home/anyone/Desktop/data_failsafe/images_foldered_filtered"
dest_dir = "/home/anyone/Desktop/data_failsafe/images_unfoldered_filtered"

for category in os.listdir(src_dir):

    for img in os.listdir(os.path.join(src_dir, category)):
        shutil.copy(os.path.join(src_dir, category, img), os.path.join(dest_dir, img))