# scripts/evaluate_model.py

import pickle
import numpy as np
from sklearn.model_selection import train_test_split
import json
import os

print("=" * 50)
print("STAGE 2: EVALUATING MODEL")
print("=" * 50)

try:
    # Load model from training job
    print("📦 Loading trained model...")
    model_path = "models/model.pkl"
    
    if not os.path.exists(model_path):
        print(f"❌ Error: {model_path} not found!")
        print("   Make sure training job completed first")
        exit(1)
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("✓ Model loaded successfully!")

    # Create test data
    print("📊 Creating test data...")
    X = np.random.randn(100, 5)
    y = np.random.randint(0, 2, 100)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Evaluate
    print("📈 Evaluating model...")
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)

    print(f"✓ Training accuracy: {train_accuracy:.2%}")
    print(f"✓ Test accuracy: {test_accuracy:.2%}")

    # Save metrics
    os.makedirs("models", exist_ok=True)
    metrics = {
        "train_accuracy": float(train_accuracy),
        "test_accuracy": float(test_accuracy),
        "n_features": X.shape[1],
        "n_samples": X.shape[0]
    }

    metrics_path = "models/metrics.json"
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)

    print(f"✓ Metrics saved to {metrics_path}")
    print("=" * 50)
    print("✅ STAGE 2 COMPLETED SUCCESSFULLY!")
    
except Exception as e:
    print(f"❌ Error in evaluation: {e}")
    exit(1)