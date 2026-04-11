from flask import Flask, render_template, request
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import os

app = Flask(__name__)

# Load stop words
# NLTK data (punkt, stopwords) is pre-installed in the Docker image
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

# Load model and vectorizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

model = None
vectorizer = None

def load_resources():
    global model, vectorizer
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        try:
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            with open(VECTORIZER_PATH, 'rb') as f:
                vectorizer = pickle.load(f)
            return True
        except Exception as e:
            print(f"Error loading resources: {e}")
            return False
    return False

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    news_text = ""
    
    if request.method == 'POST':
        news_text = request.form.get('news_text', '')
        if news_text:
            if load_resources():
                processed_text = preprocess_text(news_text)
                vectorized_text = vectorizer.transform([processed_text])
                pred = model.predict(vectorized_text)[0]
                prediction = "REAL" if pred == 1 else "FAKE"
            else:
                prediction = "Error: Model files not found. Please train the model first."
                
    return render_template('index.html', prediction=prediction, news_text=news_text)

if __name__ == '__main__':
    # Initial load attempt
    load_resources()
    app.run(host='0.0.0.0', port=5000, debug=True)
