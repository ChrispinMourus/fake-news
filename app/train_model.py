import pandas as pd
import numpy as np
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import re
import os

# Download NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

# Generate Comprehensive Synthetic Dataset
print("Generating expanded synthetic dataset...")
data_items = [
    # REAL NEWS (Label 1)
    ("The global economy showed steady growth in the third quarter, surpassing analyst expectations.", 1),
    ("NASA's latest Mars rover has successfully collected soil samples that may contain signs of ancient life.", 1),
    ("Government officials announced a new infrastructure bill aimed at improving public transportation nationwide.", 1),
    ("Scientists have discovered a new species of deep-sea jellyfish in the Pacific Ocean.", 1),
    ("Regular physical exercise is linked to improved cardiovascular health and mental well-being.", 1),
    ("The city council voted to increase funding for local libraries and community centers.", 1),
    ("Astronomers observe a distant supernova that provides new insights into the expansion of the universe.", 1),
    ("A new study published in Nature suggests that reforestation efforts are helping reduce carbon levels.", 1),
    ("The central bank maintained current interest rates to ensure economic stability.", 1),
    ("Technological advancements in solar panels have significantly reduced the cost of renewable energy.", 1),
    ("The Federal Reserve announced a small increase in interest rates yesterday to combat inflation.", 1),

    # FAKE NEWS (Label 0)
    ("Breaking: Aliens have officially taken over the national power grid and are demanding chocolate!", 0),
    ("Scientists shocked to find that drinking ocean water actually makes you immortal.", 0),
    ("The moon is actually a giant hollow balloon filled with ancient gold, secret documents reveal.", 0),
    ("New study proves that sleeping only 2 hours a day makes you a genius overnight.", 0),
    ("Celebrity secretly replaced by a robot after a minor coffee spill, sources say.", 0),
    ("Miracle cure: Rubbling onions on your toes can cure any headache in seconds!", 0),
    ("Shocking: Government plans to replace all trees with plastic versions to save water.", 0),
    ("Invisible squirrels are stealing internet bandwidth from suburban homes.", 0),
    ("A local cat has been elected mayor of a major city and plans to ban dogs.", 0),
    ("Drinking bleach is the hidden secret to eternal youth that doctors don't want you to know.", 0),
    ("Doctors discover that eating lead significantly improves memory and cognitive function.", 0),
    ("Alien invasion confirmed in major cities as flying saucers land on skyscrapers.", 0)
]

# Balance and multiply the dataset for better training stability
data = {
    'text': [item[0] for item in data_items] * 50,
    'label': [item[1] for item in data_items] * 50
}

df = pd.DataFrame(data)
df['text'] = df['text'].apply(preprocess_text)

# Vectorization with N-grams (bi-grams) to capture phrases better
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Training
print("Training model...")
model = LogisticRegression()
model.fit(X, y)

# Saving using absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

print(f"Saving model to {MODEL_PATH}...")
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model, f)

with open(VECTORIZER_PATH, 'wb') as f:
    pickle.dump(vectorizer, f)

print(f"Success! Model and vectorizer saved in {BASE_DIR}")
