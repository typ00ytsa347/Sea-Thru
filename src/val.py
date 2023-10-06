from ultralytics import YOLO
import torch

torch.cuda.set_device(0)

model = YOLO('yolov8n.yaml')

if __name__ == '__main__':
    metrics = model.val() # no arguments needed, dataset and settings remembered
    print(metrics.top1) # top1 accuracy
    print(metrics.top5) # top5 accuracy