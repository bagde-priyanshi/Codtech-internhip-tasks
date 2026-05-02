# ================================================================
# TASK 3 - END TO END DATA SCIENCE PROJECT
# CODTECH IT Solutions - Data Science Internship
# Description : Flask web app for Spam Detection
# ================================================================

import joblib
from flask import Flask, request, render_template

app = Flask(__name__)

# Load model and vectorizer once at startup
model      = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result      = None
    message     = ''
    confidence  = None
    ham_prob    = None
    spam_prob   = None
    error       = None

    if request.method == 'POST':
        
        message = request.form.get('message', '').strip()

        if not message:
            error = 'Please enter a message before checking.'
        else:
            try:
                message_vec  = vectorizer.transform([message])
                prediction   = model.predict(message_vec)[0]
                proba        = model.predict_proba(message_vec)[0]
                ham_prob     = round(proba[0] * 100, 2)
                spam_prob    = round(proba[1] * 100, 2)
                confidence   = round(max(proba) * 100, 2)
                result       = 'SPAM 🚨' if prediction == 1 else 'NOT SPAM ✅'
            except Exception as e:
                error = f'Prediction failed: {str(e)}'

    return render_template('index.html',
                           result=result,
                           message=message,
                           confidence=confidence,
                           ham_prob=ham_prob,
                           spam_prob=spam_prob,
                           error=error)

if __name__ == '__main__':
    # Set debug=False for final submission
    app.run(debug=False)
