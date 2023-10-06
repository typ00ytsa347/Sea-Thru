from ultralytics import YOLO
import torch

torch.cuda.set_device(0)

model = YOLO('yolov8n.yaml')

if __name__ == '__main__':
    results = model.train(data='data.yaml', epochs=1000, imgsz=640, batch=8, name="5Oct_imagenet_50p_8b")
    results = model.val()
    success = YOLO("yolov8n.pt").export(format="onnx")