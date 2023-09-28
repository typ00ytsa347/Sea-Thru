import os

src_dir = '/home/anyone/Documents/Sea-Thru/data/train/labels'

category_dict = dict()
name_list = list()
with open('./res/category_list.txt') as category_list:
    lines = category_list.readlines()
    count = 0
    for line in lines:
        category_dict[line.strip()] = count
        count += 1

for filename in os.listdir(src_dir):
    new_file_content = ""
    filepath = os.path.join(src_dir, filename)
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = str(line)
            parts = line.split(" ")
            parts[0] = category_dict[parts[0]]
            # parts = str(parts)
            new_line = ' '.join(map(str, parts))
            new_file_content = new_file_content + new_line
    with open(filepath, 'w') as file:
        file.write(new_file_content)
