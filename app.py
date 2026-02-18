from flask import Flask, render_template, request
from ultralytics import YOLO
import os

import uuid
from werkzeug.utils import secure_filename


""" for production level , saving file names in upload folder, agar user same name se file upload karta hai  , used in load balancing servers
uuid - Universally Unique Identifier    
secure_filename() - if user enters a dangerous filename it renames the dangerous characters """    

app = Flask(__name__)

model = YOLO("runs/classify/cow_breed_project/yolov8m_cls_exp3/weights/best.pt")

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=["POST"])
def predict():
    if "image" not in request.files:
        return "NO FILE UPLOADED"

    file = request.files["image"]

    if file.filename == "":
        return "NO FILE SELECTED"

    # --- Secure & Unique File Handling ---
    original_filename = secure_filename(file.filename)
    file_ext = os.path.splitext(original_filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_ext}"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
    file.save(filepath)

    # Prediction
    results = model(filepath)

    probs = results[0].probs
    top5 = probs.top5
    top5conf = probs.top5conf
    top_predictions = []
    
    # for showing top 3 breeds
    for i in  range(3):
        class_id = top5[i]
        confidence = top5conf[i].item()
        breed_name = results[0].names[class_id]
        
        top_predictions.append({
            "breed" : breed_name,
            "confidence" : f"{confidence:.2f}"
        })
        
    threshold = 0.60
    low_confidence = top5conf[0].item() < threshold

    return render_template(
        "index.html",
        top_predictions = top_predictions,
        low_confidence = low_confidence,
        image_path=filepath
    )



if __name__ == "__main__":
    app.run(debug=True)
