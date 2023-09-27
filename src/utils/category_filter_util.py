import os
import shutil, errno

src_path = '/home/anyone/Desktop/data_failsafe/images_foldered'
dest_path = '/home/anyone/Desktop/data_failsafe/images_foldered_filtered'

category_dict = dict()
name_list = list()
with open('./res/category_list.txt') as category_list:
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
    if name_list.__contains__(category):
        src = os.path.join(src_path, category)
        dst = os.path.join(dest_path, category)
        try:
            shutil.copytree(src, dst)
        except OSError as exc: # python >2.5
            if exc.errno in (errno.ENOTDIR, errno.EINVAL):
                shutil.copy(src, dst)
            else: raise