import os
import shutil

bb_dir = "/home/anyone/Downloads/bboxes_annotations"
turbulent_dir = "/home/anyone/Documents/sota/Machine-Learning/TurbulentWater/Water/train"

bb_dest = "/home/anyone/Documents/labelled_turbulent_images/bboxes"
turbulent_dest = "/home/anyone/Documents/labelled_turbulent_images/images"

for category in os.listdir(turbulent_dir):

    turb_category_folder = os.path.join(turbulent_dir, category)
    bb_category_folder = os.path.join(bb_dir, category, "Annotation", category)

    # make new folders
    os.makedirs(os.path.join(bb_dest, category)) 
    os.makedirs(os.path.join(turbulent_dest, category))

    for filename in os.listdir(turb_category_folder):
        turb_image_path = os.path.join(turb_category_folder, filename)
        bbox_image_path = os.path.join(bb_category_folder, filename.replace(".JPEG", ".xml"))

        if os.path.exists(bbox_image_path):
            # copy bbox file
            bbox_image_dest = os.path.join(bb_dest, category, filename.replace(".JPEG", ".xml"))
            shutil.copy(bbox_image_path, bbox_image_dest)

            # copy turbulent file
            turb_image_dest = os.path.join(turbulent_dest, category, filename)
            shutil.copy(turb_image_path, turb_image_dest)
