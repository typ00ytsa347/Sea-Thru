import os
import shutil

bb_src = "/home/anyone/Downloads/bboxes_annotations"
turb_src = "/home/anyone/Documents/sota/Machine-Learning/TurbulentWater/Water/val"

bb_dest = "/home/anyone/Documents/Sea-Thru/data/labels/val"
turb_dest = "/home/anyone/Documents/Sea-Thru/data/images/val"

for category in os.listdir(bb_src):

    bbox_category_folder = os.path.join(bb_src, category, "Annotation", category)

    for img in os.listdir(bbox_category_folder):

        turb_img_path = os.path.join(turb_src, img.replace("xml", "JPEG"))

        if os.path.exists(turb_img_path):
            # copy turbulent image
            shutil.copy(turb_img_path, turb_dest)
            # copy bbox image
            shutil.copy(os.path.join(bbox_category_folder, img), bb_dest)