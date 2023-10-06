import os
import shutil

turb_dir = "/home/anyone/Desktop/data_failsafe/turb/data_preparation/val_images_filtered"
imagenet_dir = "/home/anyone/Documents/sota/Machine-Learning/TurbulentWater/ImageNet/test/test/test"

dest = "/home/anyone/Desktop/data_failsafe/ImageNet/val"

for filename in os.listdir(turb_dir):
    turb_image_path = os.path.join(turb_dir, filename)
    imagenet_image_path = os.path.join(imagenet_dir, filename)

    if os.path.exists(imagenet_image_path):
        imagenet_image_dest = os.path.join(dest, filename)
        shutil.copy(imagenet_image_path, imagenet_image_dest)