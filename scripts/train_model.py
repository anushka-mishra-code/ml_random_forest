# scripts/train_model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

print("=" * 50)
print("STAGE 1: TRAINING MODEL")
print("=" * 50)

# Create dummy data (or load from data/data.csv)
print("📊 Loading data...")
X = np.random.randn(100, 5)
y = np.random.randint(0, 2, 100)

# Split data
print("🔀 Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
print("🤖 Training Random Forest model...")
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs("models", exist_ok=True)
model_path = "models/model.pkl"
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"✓ Model saved to {model_path}")
print(f"✓ Training accuracy: {model.score(X_train, y_train):.2%}")
print("=" * 50)