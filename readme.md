🐄 Livestock Breed Recognition System

An AI-powered web application that predicts cattle breeds from uploaded images using a trained YOLOv8 classification model.

🚀 Project Overview

This system allows users to:

Upload an image of livestock

Get Top-3 predicted breeds

View confidence scores

Receive low-confidence warnings

Experience a clean, responsive UI

Built with:

🧠 Ultralytics YOLOv8 (Classification)

🐍 Flask (Backend)

🎨 HTML + CSS (Frontend)

🗂 Production-level project structure

🏗 Project Structure
LiveStock-Detection-System/
│
├── app.py
├── train.py
├── testing_model.py
│
├── model/
│   └── best.pt   (Not included in repo)
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── uploads/
│
├── dataset/        (ignored)
├── runs/           (ignored)
├── .gitignore
└── README.md

⚠ Model Weights

Model weights (best.pt) are not included in this repository.

To run the application:

Download trained weights from:

[Add your Google Drive link here]


Place the file inside:

model/best.pt

🧠 Model Details

Model Type: YOLOv8 Classification

Training Framework: Ultralytics

Dataset: Custom cattle breed dataset

Output: Top-3 breed predictions with confidence scores

💻 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/DeepakdevilB/LiveStock-Prediction-System.git
cd LiveStock-Prediction-System

2️⃣ Create virtual environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt


If requirements.txt not present:

pip install flask ultralytics werkzeug

4️⃣ Add Model Weights

Place:

best.pt


inside:

model/

5️⃣ Run the application
python app.py


Open in browser:

http://127.0.0.1:5000

🔥 Features

✅ Production-safe file handling (UUID-based)

✅ Secure filename sanitization

✅ Top-3 breed predictions

✅ Confidence threshold warning

✅ Responsive modern UI

✅ Clean repository structure

🛠 Future Improvements

Add detection model (cow vs non-cow)

Breed information panel

Model deployment (Render / Railway)

User authentication

Prediction history logging

REST API endpoint

📌 Why Model Weights Are Not Included

Large file size

GitHub storage limits

Clean repository best practices

👨‍💻 Author

Deepak Sharma
B.Tech CSE
AI & Computer Vision Enthusiast

⭐ If You Like This Project

Star the repository and feel free to contribute!