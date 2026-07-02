import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("data/spam.csv", encoding="latin-1")

# Keep only the required columns
df = df[['v1', 'v2']]

# Rename columns
df.columns = ['label', 'message']

# Convert labels to numbers
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

# ----------------------------
# Split Data
# ----------------------------
X = df['message']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------
# Convert text into TF-IDF vectors
# ----------------------------
vectorizer = TfidfVectorizer(stop_words='english')

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# ----------------------------
# Train Model
# ----------------------------
model = MultinomialNB()

model.fit(X_train, y_train)

# ----------------------------
# Predict
# ----------------------------
predictions = model.predict(X_test)

# ----------------------------
# Accuracy
# ----------------------------
accuracy = accuracy_score(y_test, predictions)

print("=" * 40)
print("Spam Email Detector")
print("=" * 40)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# ----------------------------
# Save Model
# ----------------------------
with open("models/model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("models/vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("\n✅ Model saved successfully!")
print("✅ Vectorizer saved successfully!")