Here is your content converted into clean, copy-ready **Markdown format**:

---

```markdown
# 🌱 Syngenta Plant Disease Detection System

## 📖 Project Overview

This project implements a Deep Learning solution to assist farmers in detecting plant diseases early using computer vision. Built for the **Syngenta Mobile App AI Module**, this system utilizes **Transfer Learning** with the **EfficientNetV2B0** architecture to classify diseases in Apple, Cherry, Corn, and Blueberry plants with high accuracy (~98%).

The project includes a complete pipeline: **Data Loading, Preprocessing, Model Training (Fine-tuning), Evaluation**, and a user-friendly **Web Interface (Gradio)**.

---

## 🚀 Key Features

- **Lightweight Model:** Uses EfficientNetV2B0, optimized for mobile deployment (approx. 24MB).
- **High Accuracy:** Achieves ~98% validation accuracy.
- **10-Class Detection:** Identifies specific diseases across four different crop types.
- **Interactive App:** Includes a Gradio web interface for real-time inference.
- **Visual Evaluation:** Generates Confusion Matrices and prediction visualizations (Correct vs. Incorrect).

---

## 📂 Dataset Structure

Organize your dataset as follows inside the project root directory:

```

├── data/
│   ├── train/           # Training images (organized by class folders)
│   ├── valid/           # Validation images
│   └── test/            # Test images

````

### Supported Classes

- Apple Scab  
- Apple Black Rot  
- Apple Cedar Rust  
- Apple Healthy  
- Blueberry Healthy  
- Cherry Powdery Mildew  
- Cherry Healthy  
- Corn Gray Leaf Spot  
- Corn Common Rust  
- Corn Northern Leaf Blight  

---

## ⚙️ Installation & Requirements

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-name>
````

### 2. Install Dependencies

It's recommended to use a Python virtual environment.

```bash
pip install -r requirements.txt
```

**Required Libraries:** TensorFlow, NumPy, Matplotlib, Seaborn, Scikit-learn, Gradio.

---

## 🖥️ How to Run

### **Option 1: Running the Notebook (Training & Analysis)**

1. Open `new_main.ipynb` in Jupyter Notebook, JupyterLab, or Google Colab.
2. **Run All Cells** to execute the training pipeline.
3. Model fine-tuning uses **EfficientNetV2B0**.
4. Generates Confusion Matrix and saves the model as:

   ```
   plant_disease_model_finetuned.keras
   ```
5. Includes scripts to test unseen images in the `test/` folder.

---

### **Option 2: Running the Gradio App (Web Interface)**

You can launch an interactive app to upload leaf images and get predictions.
Run it:

```bash
python app.py
```

---

## 📊 Model Evaluation

* **Accuracy & Loss Curves:** Helps analyze overfitting/underfitting.
* **Confusion Matrix:** Shows which diseases are commonly misclassified
  (e.g., Apple Scab vs. Black Rot).
* **Confidence Thresholding:** Predictions with confidence < 60% can be treated as
  `"Unknown"` or `"Healthy"` to minimize false positives in production.

---
