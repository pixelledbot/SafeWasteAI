from torchvision import datasets
from collections import Counter
import os

DATASET_PATH = "dataset_split"

train_dataset = datasets.ImageFolder(
    os.path.join(DATASET_PATH, "train")
)

counts = Counter(train_dataset.targets)

print("\nClass Distribution:")
for idx, cls in enumerate(train_dataset.classes):
    print(f"{cls}: {counts[idx]}")