"""
Crop Disease Inference Engine
Predicts crop condition from uploaded image and retrieves comprehensive Indian agronomic solutions.
"""

import os
import json
import torch
import numpy as np
from PIL import Image

from src.model import CropDiseaseCNN
from src.solutions_db import CLASS_NAMES, INDIAN_CROP_SOLUTIONS

class CropPredictor:
    def __init__(self, model_path: str = "models/crop_disease_model.pth", metadata_path: str = "models/model_metadata.json"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.num_classes = len(CLASS_NAMES)
        self.model = CropDiseaseCNN(num_classes=self.num_classes).to(self.device)
        
        if os.path.exists(model_path):
            state = torch.load(model_path, map_location=self.device)
            self.model.load_state_dict(state)
            self.model.eval()
            print(f"[CropPredictor] Loaded trained model weights from {model_path}")
        else:
            print(f"[CropPredictor] Warning: {model_path} not found. Running initialized model.")
            
        self.metadata = {}
        if os.path.exists(metadata_path):
            with open(metadata_path, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)

    def preprocess(self, img: Image.Image) -> torch.Tensor:
        resized = img.convert("RGB").resize((224, 224), Image.Resampling.BILINEAR)
        arr = np.array(resized, dtype=np.float32).transpose((2, 0, 1)) / 255.0
        mean = np.array([0.485, 0.456, 0.406]).reshape(3, 1, 1)
        std = np.array([0.229, 0.224, 0.225]).reshape(3, 1, 1)
        norm = (arr - mean) / std
        return torch.tensor(norm, dtype=torch.float32).unsqueeze(0).to(self.device)

    def predict(self, image: Image.Image) -> dict:
        tensor = self.preprocess(image)
        
        with torch.no_grad():
            logits = self.model(tensor)
            probs = torch.softmax(logits, dim=1)[0].cpu().numpy()
            pred_idx = int(np.argmax(probs))
            conf = float(probs[pred_idx])
            
        class_name = CLASS_NAMES[pred_idx]
        sol = INDIAN_CROP_SOLUTIONS.get(class_name, INDIAN_CROP_SOLUTIONS["Healthy_Wheat_Crop"])
        
        # Top 3 differential diagnoses
        top_indices = np.argsort(probs)[::-1][:3]
        top_candidates = []
        for ti in top_indices:
            c = CLASS_NAMES[ti]
            top_candidates.append({
                "class_id": c,
                "name": INDIAN_CROP_SOLUTIONS[c]["condition_name"],
                "probability": round(float(probs[ti]) * 100, 1)
            })
            
        return {
            "class_id": class_name,
            "crop_name": sol["crop_name"],
            "condition_name": sol["condition_name"],
            "scientific_name": sol["scientific_name"],
            "category": sol["category"],
            "severity": sol["severity"],
            "severity_color": sol["severity_color"],
            "confidence_percent": round(conf * 100, 1),
            "description": sol["description"],
            "symptoms": sol["symptoms"],
            "organic_remedies": sol["organic_remedies"],
            "chemical_remedies": sol["chemical_remedies"],
            "farm_management": sol["farm_management"],
            "top_candidates": top_candidates
        }
