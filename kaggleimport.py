import kagglehub
import os
import shutil

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# List of datasets
datasets = [
    "jacksoncrow/stock-market-dataset",  # ← replace with actual Kaggle dataset id
]

for dataset in datasets:
    print(f"\nDownloading: {dataset}")
    path = kagglehub.dataset_download(dataset)
    print("Downloaded to:", path)

    # Copy CSV files to data/
    for file in os.listdir(path):
        if file.endswith(".csv"):
            src = os.path.join(path, file)
            dst = os.path.join("data", file)

            shutil.copy(src, dst)
            print(f"Copied {file} → data/")

print("\n✅ All datasets ready in /data folder")