import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import os

# Ensure NLTK data is available
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

BASE_DIR = os.path.join(os.getcwd(), 'app')
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

def test_model():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        print("Model files not found.")
        return

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)

    test_cases = [
        "Breaking: Alien invasion in New York City confirmed by government!",
        "Scientists discover a new species of frog in the Amazon rainforest.",
        "The economy is growing at a record pace this quarter",
        "Drinking bleach cures everything",
        "Doctors discover that eating lead significantly improves memory",
        "The Federal Reserve announced a small increase in interest rates yesterday"
    ]

    for text in test_cases:
        processed = preprocess_text(text)
        vectorized = vectorizer.transform([processed])
        pred = model.predict(vectorized)[0]
        label = "REAL" if pred == 1 else "FAKE"
        print(f"Text: {text[:50]}... -> Prediction: {label}")

if __name__ == "__main__":
    test_model()
