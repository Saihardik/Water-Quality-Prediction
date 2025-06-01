import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

MODEL_PATH = os.path.join("models", "model.pkl")
DATA_PATH = os.path.join("dataset", "water_potability.csv")

def train_and_save_model():
    if not os.path.exists(DATA_PATH):
        print(f"❌ Dataset not found at {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)
    df = df.dropna()

    if "Potability" not in df.columns:
        print("❌ Dataset missing required column: Potability")
        return

    X = df.drop("Potability", axis=1)
    y = df["Potability"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model trained and saved to {MODEL_PATH}")

def load_model():
    return joblib.load(MODEL_PATH)
