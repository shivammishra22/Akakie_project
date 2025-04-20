import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Load or train a simple model
def train_model():
    df = pd.read_excel("emails_dataset.xlsx")
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(df["email_body"])
    model = MultinomialNB()
    model.fit(X, df["category"])
    joblib.dump(model, "classifier.joblib")
    joblib.dump(tfidf, "vectorizer.joblib")

def predict_category(text):
    model = joblib.load("classifier.joblib")
    tfidf = joblib.load("vectorizer.joblib")
    X = tfidf.transform([text])
    return model.predict(X)[0]
