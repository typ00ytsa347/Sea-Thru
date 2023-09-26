from PIL import Image
from ultralytics import YOLO
import torch

torch.cuda.set_device(0)

model = YOLO('yolov8n.pt')

if __name__ == '__main__':
    results = model('../qh2dgs28qon41.jpg')
    for r in results:
        im_array = r.plot()
        im = Image.fromarray(im_array[..., ::-1])
        im.show()