"""
Farmer Crop Disease Detection & Remedy System - Flask Backend
"""

import os
import io
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory
from PIL import Image

from src.predictor import CropPredictor
from src.solutions_db import CLASS_NAMES, INDIAN_CROP_SOLUTIONS

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # 20 MB max file upload

os.makedirs("static/uploads", exist_ok=True)
os.makedirs("dataset/sample_images", exist_ok=True)

# Initialize predictor
predictor = CropPredictor(
    model_path="models/crop_disease_model.pth",
    metadata_path="models/model_metadata.json"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sample/<filename>")
def serve_sample(filename):
    return send_from_directory("dataset/sample_images", filename)

@app.route("/api/samples", methods=["GET"])
def get_sample_images():
    catalog_path = "dataset/sample_images/sample_catalog.json"
    if os.path.exists(catalog_path):
        try:
            with open(catalog_path, "r", encoding="utf-8") as f:
                samples = json.load(f)
            return jsonify({"success": True, "samples": samples})
        except Exception as e:
            pass
            
    # Default fallback catalog if file still generating
    fallback = []
    for c in CLASS_NAMES:
        sol = INDIAN_CROP_SOLUTIONS[c]
        fallback.append({
            "id": c.lower(),
            "name": sol["condition_name"],
            "filename": f"{c.lower()}.jpg",
            "crop": sol["crop_name"],
            "severity": sol["severity"],
            "description": sol["description"][:100] + "..."
        })
    return jsonify({"success": True, "samples": fallback})

@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        pil_image = None
        img_url = ""

        if "image" in request.files and request.files["image"].filename != "":
            file = request.files["image"]
            img_bytes = file.read()
            pil_image = Image.open(io.BytesIO(img_bytes)).convert("RGB")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_name = f"scan_{timestamp}.jpg"
            save_path = os.path.join("static/uploads", save_name)
            pil_image.save(save_path, quality=90)
            img_url = f"/static/uploads/{save_name}"

        elif request.form.get("sample_name"):
            sample_name = request.form.get("sample_name")
            sample_path = os.path.join("dataset/sample_images", sample_name)
            if os.path.exists(sample_path):
                pil_image = Image.open(sample_path).convert("RGB")
                img_url = f"/sample/{sample_name}"
            else:
                return jsonify({"success": False, "error": f"Sample image {sample_name} not found."}), 404
        else:
            return jsonify({"success": False, "error": "No crop image file or sample provided."}), 400

        # Execute prediction
        result = predictor.predict(pil_image)
        result["image_url"] = img_url
        result["timestamp"] = datetime.now().strftime("%d %b %Y, %I:%M %p")

        return jsonify({"success": True, "data": result})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Farmer Crop Disease Detection Server Online")
    print("Open in Browser: http://127.0.0.1:5000")
    print("=" * 60 + "\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
