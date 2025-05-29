# 🏗️ Architectural Arena 

This project detects **doors** and **windows** in architectural blueprints using a custom-trained YOLOv8 model and exposes a `POST /detect` API.

---

## 📂 Project Structure

.
├── images/ 
├── labels/ 
├── classes.txt # Object classes (door, window)
├── main.py # Inference API (FastAPI/Flask)
├── yolov8n.pt
├── requirements.txt
└── README.md 



---

## 🧠 Classes

doors and windows


---

## 🏷️ Labeling

- Tool: [Roboflow](https://app.roboflow.com/littleoldme)
- Format: YOLO `.txt` format
- Each image has a corresponding `.txt` file with:


<class_id> <x_center> <y_center> <width> <height>

- Example (`labels/img1.txt`):

0 0.52 0.64 0.10 0.15
1 0.33 0.27 0.20 0.10


### 🖼️ Screenshots
- 📸 `labeling_screenshot.png`: In-progress annotation in LabelImg
- 📉 `training_loss.png`: YOLO training loss graph / console output

---

## 🏋️ Training

- Framework: [Ultralytics YOLOv8](https://docs.ultralytics.com)
- Model: `yolov8n` (Nano)
- Command used:
```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
```


data.yaml content:
```bash
train: ./images/train
val: ./images/val

nc: 2
names: ['door', 'window']

```


### API Deployment Framework: FastAPI

```bash
Endpoint: POST /detect

Input: PNG or JPG image

Output:

json
Copy
Edit
{
    "detections": [
        {
            "label": "door",
            "confidence": 0.4,
            "bbox": [
                253,
                279,
                29,
                9
            ]
        },
        {
            "label": "door",
            "confidence": 0.33,
            "bbox": [
                238,
                384,
                33,
                10
            ]
        }
    ]
}
```

### Set Up Locally
```bash
git clone https://github.com/<your-username>/door-window-detector.git
cd door-window-detector

python -m venv venv
source venv/bin/activate   

pip install -r requirements.txt

python main.py            
```

### Screenshots

## first

blueprint used as input for the `/detect` API:

![Blueprint Example](https://github.com/Shrutakeerti/Architectural-Anarcy/blob/main/Screenshots/Screenshot%20(207).png)




