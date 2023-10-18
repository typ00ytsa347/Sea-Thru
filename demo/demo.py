from ultralytics import YOLO
import cv2

model = YOLO('SA-GAN.pt')

results = model('goldfish.jpg')
img = cv2.imread('goldfish.jpg')

for result in results:
    boxes = result.boxes.cpu().numpy()
    for i, box in enumerate(boxes):
        r = box.xyxy[0].astype(int)
        crop = img[r[1]:r[3], r[0]:r[2]]
        cv2.imwrite(str(i) + ".jpg", crop)