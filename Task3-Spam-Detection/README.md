# 📩 Task 3 - End-to-End Data Science Project
### CODTECH IT Solutions — Data Science Internship

---

## 📌 Overview
A complete end-to-end **Spam Detection** web application built using **Scikit-learn** for the ML model and **Flask** for deployment. Users can type any message and instantly get a prediction of whether it's spam or not, along with confidence scores.

---

## 🛠️ Tech Stack
- **Python 3.13**
- **Pandas** — Data loading and preprocessing
- **Scikit-learn** — TF-IDF Vectorizer + Naive Bayes model
- **Flask** — Web framework for deployment
- **HTML/CSS + JavaScript** — Frontend UI
- **Joblib** — Model serialization

---

## 📂 Project Structure
```
Task3-Spam-Detection/
│
├── app.py                  ← Flask web application
├── model.py                ← Model training script
├── spam_model.pkl          ← Trained Naive Bayes model
├── vectorizer.pkl          ← Saved TF-IDF vectorizer
├── requirements.txt        ← Python dependencies
├── .gitignore              ← Git ignore rules
│
├── templates/
│   └── index.html          ← Frontend webpage
│
└── static/
    └── style.css           ← Styling
```

---

## 🔄 Project Flow

```
Dataset (SMS Spam Collection)
        ↓
  Data Preprocessing
  (Label encoding, Train-Test Split)
        ↓
  TF-IDF Vectorization
  (ngram_range=(1,2), 5000 features)
        ↓
  Naive Bayes Classifier
        ↓
  Save model.pkl + vectorizer.pkl
        ↓
  Flask Web App loads model
        ↓
  User types message → Prediction returned
```

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | 97%+ |
| **Model** | Multinomial Naive Bayes |
| **Vectorizer** | TF-IDF (unigrams + bigrams) |
| **Dataset** | SMS Spam Collection (5,572 messages) |
| **Train Size** | 80% |
| **Test Size** | 20% |

---

## ✨ App Features
- ✅ Real time spam prediction with confidence score
- ✅ Shows both Ham and Spam probability
- ✅ Example messages for quick testing
- ✅ Character counter (max 500)
- ✅ Clear/Reset button
- ✅ Empty input validation
- ✅ Error handling for failed predictions
- ✅ Mobile responsive design
- ✅ Color coded results (red for spam, green for ham)

---

## 🧪 Sample Predictions

| Message | Prediction | Confidence |
|---------|-----------|------------|
| "Congratulations! You've won a free iPhone! Click now!" | SPAM 🚨 | 84.26% |
| "Hey, are we still meeting for lunch tomorrow at 1pm?" | NOT SPAM ✅ | 99.73% |
| "URGENT: Your bank account has been compromised." | SPAM 🚨 | 55.85% |

---

## ▶️ How to Run

1. Clone the repository
```bash
git clone https://github.com/bagde-priyanshi/Codtech-internhip-tasks.git
cd Codtech-internhip-tasks/Task3-Spam-Detection
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Train the model
```bash
python model.py
```

4. Run the Flask app
```bash
python app.py
```

5. Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 📜 Internship Details
- **Company** : CODTECH IT Solutions
- **Domain**  : Data Science
- **Task**    : Task 3 — End-to-End Data Science Project
- **Tools**   : Python, Scikit-learn, Flask, HTML/CSS

---

*Completion certificate will be issued on internship end date.*
