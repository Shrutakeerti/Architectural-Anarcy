from ultralytics import YOLO

<<<<<<< HEAD
def train():
    model = YOLO("yolov8n.pt")
    model.train(data="data.yaml", epochs=50)

if __name__ == "__main__":
    train()
=======

model = YOLO('yolov8n.pt')  

model.train(
    data='data.yaml',     
    epochs=30,           
    imgsz=640,          
    batch=16,           
    name='doors-windows'  
)
>>>>>>> 2d42543bc4b4a1d498c5eb81cb5440439e98bbc6
