import os
import shutil

src_dir = "/home/anyone/Downloads/IMAGENET.md"
dest_dir = "/home/anyone/Desktop/labelled_names.txt"

src_format = open(src_dir, "r")
lines = src_format.readlines()

dest_format = open(dest_dir, "w")

for line in lines:
    split_line = line.split("|")
    dest_format.write(split_line[1].strip() + ": " + split_line[2].strip() + "\n")

src_format.close()
dest_format.close()