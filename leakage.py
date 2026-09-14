import os

splits = ["train", "val", "test"]
base_path = r"c:\Users\pixel_t\Downloads\archive\dataset_split"

files = {}

for split in splits:
    files[split] = set()
    for root, _, filenames in os.walk(os.path.join(base_path, split)):
        for f in filenames:
            files[split].add(f)

# Check overlaps
print("Train-Val overlap:", len(files["train"] & files["val"]))
print("Train-Test overlap:", len(files["train"] & files["test"]))
print("Val-Test overlap:", len(files["val"] & files["test"]))