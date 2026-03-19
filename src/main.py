import torch

from data import load_data, normalize, create_dataloaders
from model import DeepMLP
from model import load_model
from train import train_model
from gui import run_app 

MODEL_PATH = "../models/mlp.pt"

def main():
    # Per riproducibilità
    torch.manual_seed(8347247)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    X_train, X_test, Y_train, Y_test = load_data("../data/all_ships.csv")

    X_train, X_test, mean, std = normalize(X_train, X_test)

    train_loader, _ = create_dataloaders(X_train, Y_train, X_test, Y_test)

    model = DeepMLP(in_features=5, hidden_units=[16, 8, 4], out_features=2)

    model, loaded = load_model(model, MODEL_PATH, device)

    if not loaded:
        print("Model not found. Training...")
        model = train_model(model, train_loader, device, MODEL_PATH)

    run_app(model, mean, std, device)

if __name__ == '__main__':
    main()