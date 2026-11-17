"""
Kisan Crop Doctor - Startup Runner
"""

from app import app

def main():
    print("=" * 60)
    print("        🌾 KISAN CROP DOCTOR - CROP DISEASE DETECTOR")
    print("   AI Disease Diagnosis & Organic + Chemical Treatment System")
    print("=" * 60)
    print("\n[INFO] Starting Web Server...")
    print("[INFO] Open your browser at: http://127.0.0.1:5000\n")
    app.run(host="0.0.0.0", port=5000, debug=False)

if __name__ == "__main__":
    main()
