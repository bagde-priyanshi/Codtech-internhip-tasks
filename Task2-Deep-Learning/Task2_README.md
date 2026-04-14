# 🎬 Task 2 - Deep Learning Project
### CODTECH IT Solutions — Data Science Internship

---

## 📌 Overview
A **Sentiment Analysis** model built using **LSTM (Long Short-Term Memory)** neural networks that classifies IMDB movie reviews as **Positive 😊 or Negative 😞**. Built using TensorFlow/Keras following industry best practices.

---

## 🛠️ Tech Stack
- **Python 3.13**
- **TensorFlow / Keras** — Building and training the LSTM model
- **NumPy** — Numerical operations
- **Matplotlib** — Training visualizations

---

## 📂 Project Structure
```
Task2-Deep-Learning/
│
├── task2_sentiment_analysis.ipynb  # Main notebook
├── sentiment_model.keras           # Trained model
├── training_history.png            # Accuracy & loss plots
└── README.md                       # Project documentation
```

---

## 🔄 Project Steps

| Step | Description |
|------|-------------|
| **1. Load Data** | Load IMDB dataset (50k reviews) built into Keras |
| **2. Explore** | Decode reviews, check lengths and label distribution |
| **3. Preprocessing** | Pad all reviews to fixed length of 200 words |
| **4. Build Model** | LSTM Neural Network with Embedding + Dropout layers |
| **5. Train** | Train with EarlyStopping to prevent overfitting |
| **6. Visualize** | Plot accuracy and loss curves over epochs |
| **7. Evaluate** | Test on 25,000 unseen reviews |
| **8. Predict** | Test with custom movie reviews |
| **9. Save** | Export trained model as `.keras` file |

---

## 🧠 Model Architecture

```
Input (200 words)
      ↓
Embedding Layer (10000 vocab → 128 dimensions)
      ↓
LSTM Layer (64 units)
      ↓
Dropout (0.3)
      ↓
Dense Layer (64 neurons, ReLU)
      ↓
Dropout (0.3)
      ↓
Dense Layer (1 neuron, Sigmoid)
      ↓
Output: Positive 😊 or Negative 😞
```

---

## 📊 Results

| Metric | Value |
|--------|-------|
| **Test Accuracy** | 86.40% |
| **Test Loss** | 0.3271 |
| **Model** | LSTM Neural Network |
| **Early Stopping** | Stopped at Epoch 4 |
| **Training samples** | 20,000 |
| **Validation samples** | 5,000 |
| **Test samples** | 25,000 |

---

## 🎯 Sample Predictions

| Review | Score | Sentiment |
|--------|-------|-----------|
| "This movie was absolutely fantastic..." | 0.9232 | Positive 😊 |
| "This was the worst movie I have ever seen..." | 0.0114 | Negative 😞 |
| "The acting was okay but the story was boring..." | 0.1555 | Negative 😞 |

---

## ✨ Key Highlights
- ✅ Used **LSTM** — captures context and word order unlike simple models
- ✅ **EarlyStopping** used to automatically prevent overfitting
- ✅ Improved test accuracy from **69% → 86%** by restoring best weights
- ✅ Model correctly handles **mixed sentiment** reviews
- ✅ Custom prediction function for real world use

---

## ▶️ How to Run

1. Install dependencies
```bash
pip install tensorflow matplotlib numpy jupyter
```

2. Launch Jupyter Notebook
```bash
jupyter notebook task2_sentiment_analysis.ipynb
```

3. Run **Kernel → Restart & Run All**

---

## 📜 Internship Details
- **Company** : CODTECH IT Solutions
- **Domain**  : Data Science
- **Task**    : Task 2 — Deep Learning Project
- **Tools**   : Python, TensorFlow, Keras

---

*Completion certificate will be issued on internship end date.*
