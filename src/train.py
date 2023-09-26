from ultralytics import YOLO
import torch

torch.cuda.set_device(0)

model = YOLO('yolov8n.yaml')

if __name__ == '__main__':
    results = model.train(data='data.yaml', epochs=50, imgsz=640, batch=16, name='50 epochs 16 batch')
    results = model.val()
    success = YOLO("yolov8n.pt").export(format="onnx")