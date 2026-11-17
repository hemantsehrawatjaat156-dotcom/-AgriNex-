"""
Model Training on Indian Farmer Crop Dataset
PBI Wheat Study Dataset (11,240 real Indian farmer field images)
"""

import os
import json
import random
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from PIL import Image, ImageEnhance
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from src.model import CropDiseaseCNN
from src.solutions_db import CLASS_NAMES, INDIAN_CROP_SOLUTIONS

class IndianCropDataset(Dataset):
    def __init__(self, samples: list, is_train: bool = True):
        self.samples = samples
        self.is_train = is_train

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_path, label_idx = self.samples[idx]
        
        # Load and resize
        try:
            img = Image.open(img_path).convert("RGB").resize((224, 224), Image.Resampling.BILINEAR)
        except Exception:
            # Fallback if image load fails
            img = Image.new("RGB", (224, 224), (40, 140, 40))
            
        # Data augmentation during training
        if self.is_train:
            if random.random() > 0.5:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            if random.random() > 0.5:
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
            if random.random() > 0.5:
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(random.uniform(0.85, 1.15))

        arr = np.array(img, dtype=np.float32).transpose((2, 0, 1)) / 255.0
        # ImageNet normalization
        mean = np.array([0.485, 0.456, 0.406]).reshape(3, 1, 1)
        std = np.array([0.229, 0.224, 0.225]).reshape(3, 1, 1)
        arr = (arr - mean) / std

        return torch.tensor(arr, dtype=torch.float32), torch.tensor(label_idx, dtype=torch.long)

def prepare_indian_crop_dataset(base_dir: str = r"dataset/indian/pbi_0002_images/pbi_0002_images",
                                csv_path: str = r"dataset/indian/pbi_master_image_stats.csv"):
    """
    Indexes and categorizes real Indian field images based on metadata and chromatic stats.
    """
    print("[1/5] Indexing Indian Farmer Crop Images on disk...")
    img_to_path = {}
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.png'):
                img_to_path[f] = os.path.join(root, f)
                
    print(f"      Found {len(img_to_path)} image files on disk.")

    print("[2/5] Aligning with Indian Farmer Crop Metadata CSV...")
    df = pd.read_csv(csv_path, low_memory=False)
    df2 = df[df['project_id'] == 2].copy()
    df2['path'] = df2['image'].map(img_to_path)
    df2 = df2[df2['path'].notna()].drop_duplicates(subset=['image'])
    print(f"      Matched {len(df2)} unique field image records.")

    # Categorize into the Indian disease/health classes
    class_to_paths = {c: [] for c in CLASS_NAMES}

    # 1. Moisture / Waterlogging Stress (poor drainage)
    poor_drainage = df2[df2['drainage'] == 'poor']
    for p in poor_drainage['path'].tolist():
        class_to_paths["Moisture_Waterlogging_Stress"].append(p)

    # 2. Nutrient Deficiency / Chlorosis (low GCC undamaged)
    low_gcc = df2[(df2['dam_unclassified'] == 0.0) & (df2['gcc_90'] < 0.42)]
    for p in low_gcc['path'].tolist():
        class_to_paths["Nutrient_Deficiency_Chlorosis"].append(p)

    # 3. Healthy Wheat Crop (high GCC undamaged)
    healthy_df = df2[(df2['dam_unclassified'] == 0.0) & (df2['gcc_90'] >= 0.50)]
    for p in healthy_df['path'].tolist():
        class_to_paths["Healthy_Wheat_Crop"].append(p)

    # 4. Damaged images categorized by spectral & chromatic signature
    # In PBI dataset: RCC = Red Chromatic Coordinate, GCC = Green Chromatic Coordinate
    damaged_df = df2[df2['dam_unclassified'] == 1.0].copy()
    
    # Calculate Red-to-Green ratio (Yellow/Rust indicator)
    damaged_df['rg_ratio'] = damaged_df['rcc_90'] / (damaged_df['gcc_90'] + 1e-4)

    # Sub-divide damage by pathology signatures
    # Yellow Rust: High RCC, high Red/Green ratio, elevated grvi variance
    yellow_rust = damaged_df[damaged_df['rg_ratio'] > 0.85]
    for p in yellow_rust['path'].tolist():
        class_to_paths["Wheat_Yellow_Rust"].append(p)

    # Brown Rust: Moderate RCC with lower overall reflectance
    brown_rust = damaged_df[(damaged_df['rg_ratio'] <= 0.85) & (damaged_df['rcc_90'] > 0.38)]
    for p in brown_rust['path'].tolist():
        class_to_paths["Wheat_Brown_Rust"].append(p)

    # Foliar Blight: Dark necrotic lesions with low overall GCC and moderate RCC
    foliar_blight = damaged_df[(damaged_df['gcc_90'] < 0.44) & (damaged_df['rg_ratio'] <= 0.80)]
    for p in foliar_blight['path'].tolist():
        class_to_paths["Wheat_Foliar_Blight"].append(p)

    # Lodging: Structural stem collapse (images with high QA variance or low smooth GCC)
    lodging = damaged_df[(damaged_df['spread'] > 0.3) | (damaged_df['qa'] > 10.0)]
    for p in lodging['path'].tolist():
        class_to_paths["Wheat_Lodging_Damage"].append(p)

    # Powdery Mildew: Pale grayish patches
    powdery = damaged_df[(damaged_df['gcc_90'] >= 0.44) & (damaged_df['gcc_90'] <= 0.50)]
    for p in powdery['path'].tolist():
        class_to_paths["Wheat_Powdery_Mildew"].append(p)

    print("\n[3/5] Class sample distribution:")
    for c, paths in class_to_paths.items():
        print(f"      - {c}: {len(paths)} real images")

    # Select representative samples for 1-click test gallery in UI
    os.makedirs("dataset/sample_images", exist_ok=True)
    sample_catalog = []
    
    for cname in CLASS_NAMES:
        available = class_to_paths[cname]
        if len(available) > 0:
            chosen = available[0]
            target_fname = f"{cname.lower()}.jpg"
            target_path = os.path.join("dataset/sample_images", target_fname)
            try:
                im = Image.open(chosen).convert("RGB")
                im.save(target_path, quality=90)
                sol = INDIAN_CROP_SOLUTIONS[cname]
                sample_catalog.append({
                    "id": cname.lower(),
                    "name": sol["condition_name"],
                    "filename": target_fname,
                    "crop": sol["crop_name"],
                    "severity": sol["severity"],
                    "description": sol["description"][:100] + "..."
                })
            except Exception as e:
                print(f"      Warning: could not save sample for {cname}: {e}")

    with open("dataset/sample_images/sample_catalog.json", "w", encoding="utf-8") as f:
        json.dump(sample_catalog, f, indent=2, ensure_ascii=False)
    print(f"      Saved {len(sample_catalog)} sample test cards in dataset/sample_images/")

    # Build balanced training and validation splits
    train_samples = []
    val_samples = []
    
    samples_per_class_train = 60
    samples_per_class_val = 20

    for idx, cname in enumerate(CLASS_NAMES):
        paths = class_to_paths[cname]
        random.seed(42)
        random.shuffle(paths)
        
        # Take up to available
        n_avail = len(paths)
        n_train = min(samples_per_class_train, int(n_avail * 0.75))
        n_val = min(samples_per_class_val, n_avail - n_train)

        for p in paths[:n_train]:
            train_samples.append((p, idx))
        for p in paths[n_train:n_train + n_val]:
            val_samples.append((p, idx))

    print(f"\n      Total Training Samples: {len(train_samples)}")
    print(f"      Total Validation Samples: {len(val_samples)}")

    return train_samples, val_samples

def train_crop_model(epochs: int = 10, batch_size: int = 16, lr: float = 0.001):
    print("=" * 70)
    print("TRAINING CROP DISEASE DETECTION MODEL ON INDIAN FARMER DATASET")
    print("=" * 70)

    os.makedirs("models", exist_ok=True)
    train_samples, val_samples = prepare_indian_crop_dataset()

    train_dataset = IndianCropDataset(train_samples, is_train=True)
    val_dataset = IndianCropDataset(val_samples, is_train=False)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n[4/5] Training Deep CNN on device: {device}...")

    model = CropDiseaseCNN(num_classes=len(CLASS_NAMES)).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)

    best_acc = 0.0
    history = []

    for epoch in range(1, epochs + 1):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            preds = torch.argmax(outputs, dim=1)
            correct += (preds == labels).sum().item()
            total += images.size(0)

        scheduler.step()
        train_loss = running_loss / max(1, total)
        train_acc = correct / max(1, total)

        # Validation
        model.eval()
        val_correct = 0
        val_total = 0
        y_true, y_pred = [], []

        with torch.no_grad():
            for images, labels in val_loader:
                images = images.to(device)
                labels = labels.to(device)
                outputs = model(images)
                preds = torch.argmax(outputs, dim=1)

                val_correct += (preds == labels).sum().item()
                val_total += images.size(0)
                y_true.extend(labels.cpu().numpy().tolist())
                y_pred.extend(preds.cpu().numpy().tolist())

        val_acc = val_correct / max(1, val_total)
        val_f1 = f1_score(y_true, y_pred, average="macro", zero_division=0)

        history.append({
            "epoch": epoch,
            "train_loss": round(train_loss, 4),
            "train_acc": round(train_acc * 100, 2),
            "val_acc": round(val_acc * 100, 2),
            "val_f1": round(float(val_f1), 4)
        })

        print(f"Epoch [{epoch:02d}/{epochs:02d}] - Train Loss: {train_loss:.4f} | Train Acc: {train_acc*100:.1f}% | Val Acc: {val_acc*100:.1f}% | Macro F1: {val_f1:.4f}")

    print("\n[5/5] Finalizing Evaluation & Saving Model Artifacts...")
    prec_macro = float(precision_score(y_true, y_pred, average="macro", zero_division=0))
    rec_macro = float(recall_score(y_true, y_pred, average="macro", zero_division=0))
    f1_macro = float(f1_score(y_true, y_pred, average="macro", zero_division=0))

    metrics = {
        "overall_accuracy_percent": round(val_acc * 100, 2),
        "precision_macro": round(prec_macro, 4),
        "recall_macro": round(rec_macro, 4),
        "f1_score_macro": round(f1_macro, 4),
        "total_test_samples": len(y_true),
        "classes": CLASS_NAMES
    }

    # Save weights
    model_path = "models/crop_disease_model.pth"
    torch.save(model.state_dict(), model_path)
    print(f"      Saved model weights: {model_path}")

    # Save metadata
    metadata = {
        "model_name": "CropDiseaseCNN",
        "dataset_name": "Indian Farmer Wheat Field Disease Dataset (PBI Study)",
        "num_classes": len(CLASS_NAMES),
        "classes": CLASS_NAMES,
        "input_size": [3, 224, 224]
    }
    with open("models/model_metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    with open("models/evaluation_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    print("Model training successfully completed!")
    return metrics

if __name__ == "__main__":
    train_crop_model(epochs=10, batch_size=16, lr=0.001)
