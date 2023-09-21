import os
import shutil

source_directories = ["/home/anyone/Downloads/train_images_1",
                      "/home/anyone/Downloads/train_images_2",
                      "/home/anyone/Downloads/train_images_3",
                      "/home/anyone/Downloads/train_images_4",]

dest_directory = "/home/anyone/Downloads/train_images_0_organised"

for source_directory in source_directories:
    for filename in os.listdir(source_directory):

        name_parts = filename.split("_")

        folder_name = name_parts[2].replace('.JPEG', '')

        new_folder_path = os.path.join(dest_directory, folder_name)
        os.makedirs(new_folder_path, exist_ok=True)

        source_file = os.path.join(source_directory, filename)

        new_filename = "_".join(name_parts[:2]) + ".JPEG"
        dest_file = os.path.join(new_folder_path, new_filename)

        shutil.move(source_file, dest_file)