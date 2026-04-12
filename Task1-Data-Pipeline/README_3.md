# 🚢 Task 1 - Data Pipeline Development
### CODTECH IT Solutions — Data Science Internship

---

## 📌 Overview
An end-to-end **ETL (Extract, Transform, Load) Pipeline** built using the Titanic dataset. The pipeline automates data preprocessing, feature engineering, model training, and evaluation using **Pandas** and **Scikit-learn** — following industry best practices.

---

## 🛠️ Tech Stack
- **Python 3.13**
- **Pandas** — Data loading and manipulation
- **Scikit-learn** — Pipeline, ColumnTransformer, RandomForestClassifier
- **Matplotlib & Seaborn** — Visualizations
- **Joblib** — Model saving

---

## 📂 Project Structure
```
task1_etl_pipeline/
│
├── task1_etl_pipeline.ipynb   # Main notebook with full pipeline
├── titanic.csv                # Raw dataset
├── titanic_cleaned.csv        # Cleaned & transformed dataset
├── model.pkl                  # Trained pipeline saved with joblib
├── eda_plots.png              # EDA visualizations
├── confusion_matrix.png       # Model evaluation plot
├── feature_importance.png     # Top 10 feature importances
└── README.md                  # Project documentation
```

---

## 🔄 Pipeline Steps

| Step | Description |
|------|-------------|
| **1. Extract** | Load raw Titanic dataset from CSV |
| **2. Explore** | Inspect shape, data types, missing values, statistics |
| **3. Visualize** | EDA plots — survival count, age distribution, class survival rate |
| **4. Feature Engineering** | Create `FamilySize`, `IsAlone`, and `Title` from existing columns |
| **5. Data Cleaning** | Drop low-value columns (Cabin, Ticket, PassengerId, Name) |
| **6. Train-Test Split** | 80/20 split with `stratify=y` to preserve class balance |
| **7. Pipeline Creation** | `ColumnTransformer` with `SimpleImputer` + `OneHotEncoder` + `RandomForestClassifier` |
| **8. Model Training** | Fit pipeline on training data only (no data leakage) |
| **9. Evaluation** | Accuracy, Classification Report, Confusion Matrix, Feature Importance |
| **10. Save Outputs** | Export cleaned CSV and trained model as `model.pkl` |

---

## 📊 Results

| Metric | Score |
|--------|-------|
| **Accuracy** | ~81% |
| **Model** | RandomForestClassifier (100 estimators) |
| **Train Size** | 712 samples |
| **Test Size** | 179 samples |

---

## ✨ Key Highlights
- ✅ All preprocessing handled **inside the pipeline** — no data leakage
- ✅ Used `OneHotEncoder` instead of `LabelEncoder` for proper categorical encoding
- ✅ Removed `StandardScaler` — not needed for tree-based models
- ✅ Used `stratify=y` in train-test split for balanced evaluation
- ✅ Engineered new features: `FamilySize`, `IsAlone`, `Title`
- ✅ Feature importance visualization for model explainability

---

## ▶️ How to Run

1. Clone the repository
```bash
git clone https://github.com/your-username/CODTECH-Data-Science-Internship.git
cd CODTECH-Data-Science-Internship/Task1
```

2. Install dependencies
```bash
pip install pandas scikit-learn matplotlib seaborn joblib jupyter
```

3. Launch Jupyter Notebook
```bash
jupyter notebook task1_etl_pipeline.ipynb
```

4. Run **Kernel → Restart & Run All**

---

## 📜 Internship Details
- **Company** : CODTECH IT Solutions
- **Domain**  : Data Science
- **Task**    : Task 1 — Data Pipeline Development
- **Tools**   : Python, Pandas, Scikit-learn

---

*Completion certificate will be issued on internship end date.*
