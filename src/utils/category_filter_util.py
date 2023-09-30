import os
import shutil, errno

src_path = '/home/anyone/Desktop/data_failsafe/turb/images_foldered'
dest_path = '/home/anyone/Desktop/data_failsafe/zmurez/restoration/train_images_filtered'

label_src_path = '/home/anyone/Desktop/data_failsafe/turb/val_labels_txt'
label_dest_path = '/home/anyone/Desktop/data_failsafe/turb/val_labels_filtered_txt'

category_dict = dict()
name_list = list()
with open('./res/test.txt') as category_list:
    lines = category_list.readlines()
    count = 0
    for line in lines:
        category_dict[count] = line.strip()
        count += 1

with open('./res/aquatic_category_list.txt') as aquatic_category_list:
    lines = aquatic_category_list.readlines()
    for line in lines:
        parts = line.split(':')
        key = int(parts[0])
        name_list.append(category_dict[key])

for category in os.listdir(src_path):
    for filename in os.listdir(os.path.join(src_path, category)):
        # category = filename.split("_")[0]
        if category not in name_list:
            src = os.path.join(src_path, category, filename)
            dst = os.path.join(dest_path, filename)
            try:
                shutil.copy(src, dst)
            except OSError as exc: # python >2.5
                if exc.errno in (errno.ENOTDIR, errno.EINVAL):
                    shutil.copy(src, dst)
                else: raise

for filename in os.listdir(label_src_path):
    category = filename.split("_")[0]
    if name_list.__contains__(category):
        src = os.path.join(label_src_path, filename)
        dst = os.path.join(label_dest_path, filename)
        try:
            shutil.copy(src, dst)
        except OSError as exc: # python >2.5
            if exc.errno in (errno.ENOTDIR, errno.EINVAL):
                shutil.copy(src, dst)
            else: raise