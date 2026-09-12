import json
import os

print("=" * 60)
print("STAGE 3: DEPLOYMENT")
print("=" * 60)

# Check metrics
print("🔍 Checking model metrics...")
try:
    with open("models/metrics.json", 'r') as f:
        metrics = json.load(f)
    print("✓ Metrics found!")
    print(f"  Train accuracy: {metrics['train_accuracy']:.2%}")
    print(f"  Test accuracy: {metrics['test_accuracy']:.2%}")
except FileNotFoundError:
    print("❌ Error: models/metrics.json not found!")
    exit(1)

# Check quality
MIN_ACCURACY = 0.5
test_acc = metrics['test_accuracy']

if test_acc >= MIN_ACCURACY:
    print(f"\n✅ Quality check PASSED!")
    print(f"   Accuracy {test_acc:.2%} >= threshold {MIN_ACCURACY:.2%}")
    print("🚀 Model ready for deployment!")
    print("=" * 60)
    print("✅ STAGE 3 COMPLETED!")
    print("✅ ENTIRE PIPELINE SUCCESSFUL!")
else:
    print(f"\n❌ Quality check FAILED!")
    print(f"   Accuracy {test_acc:.2%} < threshold {MIN_ACCURACY:.2%}")
    print("   Model NOT deployed!")
    exit(1)