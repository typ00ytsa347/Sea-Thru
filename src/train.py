from ultralytics import YOLO

model = YOLO('yolov8n.yaml')
results = model.train(data='data.yaml', epochs=10)