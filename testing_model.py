from ultralytics import YOLO

model = model = YOLO("runs/classify/cow_breed_project/yolov8m_cls_exp3/weights/best.pt")

if __name__=="__main__":
    
    model.predict(
        source="Testing_Images/holstein_test.jpg",
        show=True,
        save=True
    )

    model.predict(source="Testing_Images/gir_test.jpg",show=True,save=True)
    model.predict(source="Testing_Images/holstein_test.jpg",show=True,save=True)
    model.predict(source="Testing_Images/holstein_test2.jpg",show=True,save=True)
    model.predict(source="Testing_Images/holstein_test3.jpg",show=True,save=True)
    model.predict(source="Testing_Images/holstein_test4.jpg",show=True,save=True)
    model.predict(source="Testing_Images/holstein_test5.jpg",show=True,save=True)
    model.predict(source="Testing_Images/ongole_test.jpg",show=True,save=True)
    model.predict(source="Testing_Images/ongole_test2.jpg",show=True,save=True)
    model.predict(source="Testing_Images/sahiwal_test.jpg",show=True,save=True)
    model.predict(source="Testing_Images/sahiwal_test2.jpg",show=True,save=True)
    model.predict(source="Testing_Images/tharparkar_test.jpg",show=True,save=True)
    model.predict(source="Testing_Images/tharparkar_test2.jpg",show=True,save=True)
    model.predict(source="Testing_Images/tharparkar_test3.jpg",show=True,save=True)