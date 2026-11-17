"""
Train Crop Disease Model on Indian Farmer Dataset
"""

from src.train import train_crop_model

def main():
    print("Starting Training on Indian Farmer Crop Dataset (C:\\Users\\Heman\\OneDrive\\Desktop\\cs\\dataset\\indian)...")
    metrics = train_crop_model(epochs=10, batch_size=16, lr=0.001)
    print("\nTraining Complete!")
    print(f"Accuracy: {metrics['overall_accuracy_percent']}%")
    print(f"F1 Score: {metrics['f1_score_macro']}")
    print("Model saved to: models/crop_disease_model.pth")

if __name__ == "__main__":
    main()
