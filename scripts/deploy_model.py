# scripts/deploy_model.py

import json
import os

print("=" * 50)
print("STAGE 3: DEPLOYMENT")
print("=" * 50)

# Check if metrics exist
print("🔍 Checking model metrics...")
try:
    with open("models/metrics.json", 'r') as f:
        metrics = json.load(f)
    print("✓ Metrics found!")
    print(f"  - Train accuracy: {metrics['train_accuracy']:.2%}")
    print(f"  - Test accuracy: {metrics['test_accuracy']:.2%}")
except FileNotFoundError:
    print("❌ Error: metrics.json not found!")
    print("   Make sure evaluation job completed first")
    exit(1)

# Check quality threshold
test_acc = metrics['test_accuracy']
MIN_ACCURACY = 0.5

if test_acc >= MIN_ACCURACY:
    print(f"\n✅ Quality check PASSED (accuracy: {test_acc:.2%})")
    print("🚀 Ready for deployment!")
    print("\nIn real production:")
    print("  - Upload model to AWS S3")
    print("  - Deploy to API server")
    print("  - Update monitoring dashboard")
else:
    print(f"\n❌ Quality check FAILED (accuracy: {test_acc:.2%})")
    print(f"   Required: {MIN_ACCURACY:.2%}")
    print("   Model NOT deployed!")
    exit(1)

print("=" * 50)