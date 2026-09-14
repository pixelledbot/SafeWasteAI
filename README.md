# SafeWaste AI – Hospital Waste Classification System

## OVERVIEW

SafeWaste AI is an AI-powered hospital biomedical waste classification system developed using Flask, PyTorch, and Deep Learning.  
The system classifies hospital waste images into different biomedical categories and provides disposal instructions instantly.

The project uses a fine-tuned ResNet-18 deep learning model trained on biomedical waste images and includes Grad-CAM heatmap visualization for explainable AI predictions.
---
Here is the project demo video link : https://youtu.be/64LebJqiT9E :) 

---

# FEATURES

- AI-powered biomedical waste classification
- Real-time image prediction
- Upload image from device
- Live camera capture support
- Image cropping before prediction
- Grad-CAM heatmap visualization
- Prediction confidence score
- Automatic disposal instructions
- Dashboard analytics
- SQLite database integration
- PDF report export with images
- Email report generation
- Automatic low-confidence email alerts
- Feedback correction system
- Responsive modern UI
- Test Accuracy of 98.71 

---

# WASTE CATEGORIES

| Category | Risk Level | Disposal Method |
|----------|-------------|----------------|
| General | Low | Black Bin |
| Infectious | High | Yellow Bin |
| Pharmaceutical | Medium | Blue Bin |
| Sharps | Critical | White Container |

---

# TECHNOLOGIES USED

## Frontend
- HTML
- CSS
- JavaScript
- Cropper.js

## Backend
- Flask
- SQLite
- Flask-Mail

## AI / Deep Learning
- PyTorch
- TorchVision
- ResNet-18
- Grad-CAM
- OpenCV

## Report Generation
- ReportLab PDF

---

# PROJECT STRUCTURE

```bash
SafeWaste-AI/
│
├── app.py
├── training.py
├── database.db
├── classes.pth
├── waste_classifier_best.pth
├── requirements.txt
│
├── templates/
│   ├── home.html
│   ├── upload.html
│   ├── result.html
│   ├── dashboard.html
│   ├── who.html
│   ├── biomedical.html
│   ├── privacy.html
│   └── terms.html
│
├── static/
│   ├── style.css
│   ├── logo.png
│   └── uploads/
│
├── dataset_split/
│   ├── train/
│   ├── val/
│   └── test/
│
└── README.md
```
The files in .gitignore are not included in this repository due to large size or irrelevance.
The dataset was taken from Kaggle.
---

# HOW THE SYSTEM WORKS

## Step 1 — Upload or Capture Image
User uploads an image or captures waste using live camera.

## Step 2 — Image Preprocessing
The image is resized to:

```python
224 × 224
```

and normalized using ImageNet normalization.

## Step 3 — AI Prediction
The ResNet-18 model predicts the waste category.

## Step 4 — Confidence Calculation
Softmax probabilities are used to calculate prediction confidence.

## Step 5 — Grad-CAM Heatmap
A heatmap is generated showing which image regions influenced the prediction.

## Step 6 — Database Storage
Prediction history is stored in SQLite database.

## Step 7 — PDF & Email Reports
Reports are generated with:
- prediction data
- confidence
- timestamps
- actual waste images

---

# DEEP LEARNING MODEL

## Model Architecture

- Base Model: ResNet-18
- Framework: PyTorch
- Transfer Learning: Enabled
- Fine-Tuning: Layer3 + Layer4 + FC Layer

---

# MODEL TRAINING

## Training Techniques Used

- Transfer Learning
- Data Augmentation
- Label Smoothing
- AdamW Optimizer
- Cosine Annealing Scheduler

---

# IMAGE AUGMENTATION

```python
RandomHorizontalFlip
RandomRotation
ColorJitter
Resize
Normalization
```

---

# TRAINING DETAILS

| Parameter | Value |
|-----------|------|
| Epochs | 8 |
| Batch Size | 16 |
| Optimizer | AdamW |
| Learning Rate | 0.0003 |
| Loss Function | CrossEntropyLoss |
| Scheduler | CosineAnnealingLR |

---

# EXPLAINABLE AI (Grad-CAM)

The system generates Grad-CAM heatmaps to visualize:
- model attention areas
- important image regions
- prediction reasoning

This improves transparency and trust in AI predictions.

---

# EMAIL SYSTEM

The project includes automatic email functionality.

## Features

- Send dashboard PDF reports via email
- Attach generated PDF automatically
- Send low-confidence prediction alerts
- Attach suspicious waste image in alert mail

---

# PDF REPORT FEATURES

Generated reports include:

- Total predictions
- Average confidence
- Waste category counts
- Full prediction history
- Waste images
- Prediction confidence
- Timestamps

---

# DATABASE

SQLite database stores:

## History Table
- filename
- prediction
- confidence
- timestamp

## Feedback Table
- corrected labels
- prediction corrections
- confidence
- timestamps

---

# DASHBOARD FEATURES

- Total scans
- Prediction history
- Waste category statistics
- Last updated timestamp
- Multi-delete records
- Report export

---

# CAMERA FEATURES

- Live camera capture
- Real-time preview
- Crop captured image
- Mobile camera support
- Webcam support

---

# SECURITY FEATURES

- File validation
- Secure image handling
- Database protection
- Controlled uploads
- Error handling

---

# INSTALLATION

## Step 1 — Clone Project

```bash
git clone https://github.com/yourusername/safewaste-ai.git
cd safewaste-ai
```

---

## Step 2 — Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Add Model Files

Place these files in root directory:

```bash
classes.pth
waste_classifier_best.pth
```

---

## Step 5 — Run Application

```bash
python app.py
```

---

# ACCESS APPLICATION (not deployed yet)

Open browser:

```bash
http://127.0.0.1:5000
```

---

# TRAIN MODEL

Run:

```bash
python training.py
```

The trained model will be saved as:

```bash
waste_classifier_best.pth
```

---

# REQUIREMENTS

```txt
flask
torch
torchvision
opencv-python
numpy
pillow
flask-mail
reportlab
```

---

# FUTURE IMPROVEMENTS

- Multi-waste detection
- Real-time CCTV integration
- Voice assistant support
- Cloud deployment
- Mobile application
- IoT smart bin integration

---

# DEVELOPERS

Developed by Simran Kaur, Simran Kaur and Harjot Kaur

---

# LICENSE

This project is developed for educational and research purposes.

---

# 🏥 SafeWaste AI

AI for safer biomedical waste management.
