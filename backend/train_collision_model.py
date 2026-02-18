import pandas as pd
import numpy as np
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

class SatelliteDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)
    def __len__(self):
        return len(self.X)
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

class CollisionMLP(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )
    def forward(self, x):
        return self.model(x)

if __name__ == "__main__":
    print("🚀 Starting training...")

    df = pd.read_csv("satellite_ai_dataset_fast.csv")
    print(f"Dataset loaded: {len(df)} satellites")

    feature_cols = ["x","y","z","vx","vy","vz","inclination","eccentricity",
                    "RAAN","argument_of_perigee","mean_anomaly","mean_motion"]
    X = df[feature_cols].values
    y = df["collision_label"].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    train_dataset = SatelliteDataset(X_train, y_train)
    test_dataset  = SatelliteDataset(X_test, y_test)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader  = DataLoader(test_dataset, batch_size=64, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CollisionMLP(input_dim=X.shape[1]).to(device)
    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    epochs = 5  
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for batch_X, batch_y in train_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device).unsqueeze(1)
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * batch_X.size(0)
        print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss/len(train_loader.dataset):.6f}")

    
    model.eval()
    correct = 0
    with torch.no_grad():
        for batch_X, batch_y in test_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device).unsqueeze(1)
            outputs = model(batch_X)
            preds = (outputs > 0.5).float()
            correct += (preds == batch_y).sum().item()
    accuracy = correct / len(test_dataset)
    print(f"✅ Test Accuracy: {accuracy*100:.2f}%")

    
    torch.save(model.state_dict(), "collision_mlp_model.pt")
    joblib.dump(scaler, "feature_scaler.pkl")
    print("✅ Model and scaler saved successfully!")
