import pickle
import numpy as np
from sklearn.model_selection import train_test_split
import json
import os

print("=" * 60)
print("STAGE 2: EVALUATING MODEL")
print("=" * 60)

# Load model
print("📦 Loading trained model...")
try:
    with open("models/model.pkl", 'rb') as f:
        model = pickle.load(f)
    print("✓ Model loaded successfully!")
except FileNotFoundError:
    print("❌ Error: models/model.pkl not found!")
    exit(1)

# Create test data
print("📊 Creating test data...")
X = np.random.randn(100, 5)
y = np.random.randint(0, 2, 100)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Evaluate
print("📈 Evaluating model...")
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print(f"✓ Training accuracy: {train_acc:.2%}")
print(f"✓ Test accuracy: {test_acc:.2%}")

# Save metrics
os.makedirs("models", exist_ok=True)
metrics = {
    "train_accuracy": float(train_acc),
    "test_accuracy": float(test_acc)
}

with open("models/metrics.json", 'w') as f:
    json.dump(metrics, f, indent=2)

print("✓ Metrics saved to models/metrics.json")
print("=" * 60)
print("✅ STAGE 2 COMPLETED!")