import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torchvision.models import resnet18
from torch.utils.data import DataLoader

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt

# ---------------- SETTINGS ----------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

IMG_SIZE = 224

MODEL_PATH = "waste_classifier_best.pth"
TEST_PATH = "dataset_split/test"

# ---------------- TRANSFORM ----------------

transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])

# ---------------- DATASET ----------------

test_dataset = datasets.ImageFolder(
    TEST_PATH,
    transform=transform
)

test_loader = DataLoader(
    test_dataset,
    batch_size=16,
    shuffle=False
)

# ---------------- MODEL ----------------

model = resnet18()

model.fc = nn.Linear(
    model.fc.in_features,
    4
)

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=device
    )
)

model.to(device)
model.eval()

# ---------------- TESTING ----------------

all_preds = []
all_labels = []

with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device)

        outputs = model(images)

        _, preds = torch.max(outputs, 1)

        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.numpy())

# ---------------- ACCURACY ----------------

correct = sum(
    p == l
    for p, l in zip(all_preds, all_labels)
)

accuracy = 100 * correct / len(all_labels)

print(f"\nTest Accuracy: {accuracy:.2f}%\n")

# ---------------- REPORT ----------------

print(
    classification_report(
        all_labels,
        all_preds,
        target_names=test_dataset.classes
    )
)

# ---------------- CONFUSION MATRIX ----------------

cm = confusion_matrix(
    all_labels,
    all_preds
)

print("\nConfusion Matrix:\n")
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=test_dataset.classes
)

disp.plot()

plt.title("Confusion Matrix")
plt.show()