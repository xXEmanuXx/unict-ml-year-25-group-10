import pandas as pd
import torch
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split

def load_data(path):
    df = pd.read_csv(path)

    X = df[["sex", "age", "age_missing", "class", "crew"]]
    Y = df["survived"]

    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    Y_tensor = torch.tensor(Y.values, dtype=torch.long) # La CrossEntropyLoss richiede target long

    # per riproducibilità si usa random_state fissato
    X_train, X_test, Y_train, Y_test = train_test_split(X_tensor, Y_tensor, test_size=0.2, random_state=42, stratify=Y_tensor)

    return X_train, X_test, Y_train, Y_test

def normalize(X_train, X_test):
    mean = X_train.mean(0)
    std = X_train.std(0)

    X_train_norm = (X_train - mean) / std
    X_test_norm = (X_test - mean) / std

    return X_train_norm, X_test_norm, mean, std

def create_dataloaders(X_train, Y_train, X_test, Y_test, batch_train=32, batch_test=64):

    train_ds = TensorDataset(X_train, Y_train)
    test_ds = TensorDataset(X_test, Y_test)

    train_loader = DataLoader(train_ds, batch_size=batch_train, shuffle=True)
    test_loader = DataLoader(test_ds, batch_size=batch_test)

    return train_loader, test_loader