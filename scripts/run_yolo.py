import os
from ultralytics import YOLO
import json

model = YOLO("yolov8n.pt")

input_dir = "data/images"
output = []

for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith(".jpg"):
            path = os.path.join(root, file)
            results = model(path)

            for r in results:
                for box in r.boxes:
                    output.append({
                        "image_path": path,
                        "class_id": int(box.cls),
                        "confidence": float(box.conf),
                        "detected_object": model.names[int(box.cls)],
                    })

with open("data/image_detections.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ YOLO detections saved to image_detections.json")
