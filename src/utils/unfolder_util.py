import os
import shutil

src_dir = "/home/anyone/Documents/Sea-Thru/data/labels/train_foldered"
dest_dir = "/home/anyone/Documents/Sea-Thru/data/labels/train"

for category in os.listdir(src_dir):

    for img in os.listdir(os.path.join(src_dir, category)):
        shutil.copy(os.path.join(src_dir, category, img), os.path.join(dest_dir, img))