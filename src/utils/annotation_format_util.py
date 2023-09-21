import os
import xml.etree.ElementTree as ET

def main():
    src_path = "/home/anyone/Documents/Sea-Thru/data/labels/train"
    dest_path = "/home/anyone/Desktop"

    for filename in os.listdir(src_path):
        src_annotation_path = os.path.join(src_path, filename)
        dest_annotation_path = os.path.join(dest_path, filename)

        parse_xml(src_annotation_path, dest_annotation_path)


def parse_xml(xml_path, write_path):
    dest_file = open(write_path, "w")

    # create element tree object
    tree = ET.parse(xml_path)
  
    # get root element
    root = tree.getroot()
  
    for child in root:
        category
        img_width, img_height
        xmin, ymin, xmax, ymax

        if child.tag == "size":
            img_width = int(child[0].text)
            img_height = int(child[1].text)
        if child.tag == "object":
            for grandchild in child:
                if grandchild.tag == "name":
                    category = grandchild.text
                if grandchild.tag == "bndbox":
                    xmin = int(grandchild[0].text)
                    ymin = int(grandchild[1].text)
                    xmax = int(grandchild[2].text)
                    ymax = int(grandchild[3].text)
            xcentre, ycentre, width, height = calc_xywh()

            x, y, w, h = str(xcentre), str(ycentre), str(width), str(height)

            line = " ".join(category, x, y, w, h) + "\n"

            dest_file.write(line)
    dest_file.close()


def calc_xywh(img_width, img_height, xmin, ymin, xmax, ymax):
    x = (xmin + xmax) / 2.0
    xnorm = x / img_width

    y = (ymin + ymax) / 2.0
    ynorm = y / img_height

    w = float(xmax - xmin)
    wnorm = w / img_width

    h = float(ymax - ymin)
    hnorm = h / img_height

    return xnorm, ynorm, wnorm, hnorm

if __name__ == "__main__":
    main()