from ultralytics import YOLO

def main():
    
    # loading pre-trained YOLOv8 model classification wala
    
    model = YOLO("yolov8s-cls.pt")      
    # this is small model , medium wala model google colab se train krke better aaya hai 
    
    # Training
    
    model.train(
        data = "dataset",
        epochs = 30,
        imgsz = 320,
        batch = 16,
        lr0 = 0.001,
        patience = 10,
        device = "cpu",
        project="cow_breed_project",
        name="yolov8s_cls_exp2"
    )
    

if __name__ == "__main__":
    main()
    
    
    