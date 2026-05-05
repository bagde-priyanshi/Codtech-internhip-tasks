# 🎓 CODTECH IT Solutions — Data Science Internship
### Internship Tasks Repository

---

## 👩‍💻 Intern Details
- **Name**    : Priyanshi Bagde
- **Company** : CODTECH IT Solutions
- **Domain**  : Data Science
- **Tasks**   : 4 out of 4 Completed ✅

---

## 📌 Overview
This repository contains all four Data Science internship tasks completed during the CODTECH IT Solutions internship program. Each task covers a different real-world data science skill — from building ETL pipelines to deploying ML models as web applications.

---

## 📂 Repository Structure
```
Codtech-internship-tasks/
│
├── Task1-Data-Pipeline/
│   ├── task1_etl_pipeline.ipynb
│   ├── titanic.csv
│   ├── titanic_cleaned.csv
│   ├── model.pkl
│   └── README.md
│
├── Task2-Deep-Learning/
│   ├── task2_sentiment_analysis.ipynb
│   ├── sentiment_model.keras
│   ├── best_model.keras
│   ├── training_history.png
│   ├── confusion_matrix.png
│   ├── eda_plots.png
│   └── README.md
│
├── Task3-Spam-Detection/
│   ├── app.py
│   ├── model.py
│   ├── spam_model.pkl
│   ├── vectorizer.pkl
│   ├── confusion_matrix.png
│   ├── requirements.txt
│   ├── .gitignore
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│   └── README.md
│
├── Task4-Optimization-Model/
│   ├── task4_optimization.ipynb
    ├── task4_optimization.py
│   ├── optimization_results.png
│   └── README.md
│
└── README.md
```

---

## 🗂️ Tasks Summary

### ✅ Task 1 — Data Pipeline Development
> Build an ETL pipeline using Pandas and Scikit-learn

- **Dataset**  : Titanic (891 passengers)
- **Pipeline** : Extract → Clean → Transform → Train → Save
- **Model**    : Random Forest Classifier
- **Accuracy** : 81%
- **Key Skills**: Pandas, ColumnTransformer, OneHotEncoder, Feature Engineering

---

### ✅ Task 2 — Deep Learning Project
> Sentiment Analysis on movie reviews using LSTM Neural Network

- **Dataset**  : IMDB Movie Reviews (50,000 reviews)
- **Model**    : LSTM Neural Network (TensorFlow/Keras)
- **Accuracy** : 86.40%
- **Key Skills**: Deep Learning, NLP, Embeddings, EarlyStopping, Keras

---

### ✅ Task 3 — End-to-End Data Science Project
> Spam Detection web app deployed using Flask

- **Dataset**  : SMS Spam Collection (5,572 messages)
- **Model**    : Multinomial Naive Bayes + TF-IDF
- **Accuracy** : 97%+
- **Key Skills**: Flask, Scikit-learn, TF-IDF, HTML/CSS, Model Deployment

---

### ✅ Task 4 — Optimization Model
> Product Mix Optimization using Linear Programming

- **Problem**  : Maximize factory profit given limited resources
- **Library**  : PuLP
- **Result**   : $4,820 maximum profit (10 Chairs + 36 Tables)
- **Key Skills**: Linear Programming, PuLP, Scenario Analysis, Visualization

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| **Languages** | Python 3.13 |
| **Data** | Pandas, NumPy |
| **ML** | Scikit-learn, TensorFlow, Keras |
| **Optimization** | PuLP |
| **Deployment** | Flask, HTML, CSS |
| **Visualization** | Matplotlib, Seaborn |
| **Model Saving** | Joblib, Keras |

---

## ▶️ How to Run Each Task

```bash
# Clone the repository
git clone https://github.com/bagde-priyanshi/Codtech-internhip-tasks.git
cd Codtech-internhip-tasks

# Task 1 - Open in Jupyter
cd Task1-Data-Pipeline
jupyter notebook task1_etl_pipeline.ipynb

# Task 2 - Open in Jupyter
cd Task2-Deep-Learning
jupyter notebook task2_sentiment_analysis.ipynb

# Task 3 - Run Flask App
cd Task3-Spam-Detection
pip install -r requirements.txt
python model.py
python app.py
# Open http://127.0.0.1:5000

# Task 4 - Open in Jupyter
cd Task4-Optimization-Model
jupyter notebook task4_optimization.ipynb
```

---

## 📊 Results at a Glance

| Task | Problem | Model | Result |
|------|---------|-------|--------|
| Task 1 | Survival Prediction | Random Forest | 81% Accuracy |
| Task 2 | Sentiment Analysis | LSTM | 86.40% Accuracy |
| Task 3 | Spam Detection | Naive Bayes | 97%+ Accuracy |
| Task 4 | Profit Maximization | Linear Programming | $4,820 Max Profit |

---

*Completion certificate will be issued on internship end date.*
