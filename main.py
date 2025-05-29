from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
import io
import uvicorn
import torch

app = FastAPI()


model = YOLO(r"runs\detect\train3\weights\best.pt")  

@app.post("/detect")
async def detect(file: UploadFile = File(...)):

    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    
    results = model(image)

    detections = []
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = results[0].names[cls_id]
        conf = float(box.conf[0])
        x1, y1, x2, y2 = box.xyxy[0]
        x, y, w, h = float(x1), float(y1), float(x2 - x1), float(y2 - y1)
        detections.append({
            "label": label,
            "confidence": round(conf, 2),
            "bbox": [round(x), round(y), round(w), round(h)]
        })

    return JSONResponse(content={"detections": detections})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
