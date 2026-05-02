# ================================================================
# model.py
# TASK 3 - END TO END DATA SCIENCE PROJECT
# CODTECH IT Solutions - Data Science Internship
# Description : Train and save Spam Detection model
# ================================================================

import pandas as pd
import joblib
import requests
import io
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# ================================================================
# STEP 1: LOAD DATASET
# SMS Spam Collection dataset from UCI repository
# Contains 5572 real SMS messages - spam or ham (not spam)
# ================================================================

url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df  = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

print(f"✅ Dataset loaded! Shape: {df.shape}")
print(df['label'].value_counts())

# ================================================================
# STEP 2: PREPROCESS
# Convert labels to numbers: ham=0, spam=1
# ================================================================

df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['message']
y = df['label']

# ================================================================
# STEP 3: SPLIT DATA
# 80% training, 20% testing
# stratify=y preserves spam/ham ratio in both splits
# ================================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training samples : {len(X_train)}")
print(f"Testing samples  : {len(X_test)}")

# ================================================================
# STEP 4: VECTORIZE TEXT
# TF-IDF converts text into numbers the model can understand
# TF  = how often a word appears in THIS message
# IDF = how rare the word is across ALL messages
# Rare but frequent words in a message = more important
# ================================================================

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)

# ================================================================
# STEP 5: TRAIN MODEL
# Naive Bayes works extremely well for text classification
# It's fast, simple and great for spam detection
# ================================================================

model = MultinomialNB()
model.fit(X_train_vec, y_train)

# ================================================================
# STEP 6: EVALUATE
# ================================================================

y_pred = model.predict(X_test_vec)
print(f"\n✅ Accuracy : {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))

# ================================================================
# STEP 7: SAVE MODEL AND VECTORIZER
# Both need to be saved - model for prediction
# vectorizer to convert new messages the same way
# ================================================================

joblib.dump(model, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("✅ Model saved as spam_model.pkl")
print("✅ Vectorizer saved as vectorizer.pkl")