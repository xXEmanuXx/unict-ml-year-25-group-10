import torch
from torch import nn
from torch.optim import SGD
import os

def train_model(model, train_loader, device, save_path, lr=0.05, epochs=300):
    model = model.to(device)

    weights = torch.tensor([1.0, 2.0]).to(device)
    criterion = nn.CrossEntropyLoss(weight=weights)
    optimizer = SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=0.001)

    for epoch in range(epochs):
        model.train()
        
        for X_batch, Y_batch in train_loader:
            X_batch = X_batch.to(device)
            Y_batch = Y_batch.to(device)

            output = model(X_batch)
            loss = criterion(output, Y_batch)

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

        if epoch % 50 == 0:
            print(f"Epoch {epoch+1}/{epochs} complete")

    print(f"Epoch {epoch+1}/{epochs} complete\n")

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    torch.save(model.state_dict(), save_path)

    print(f"Model saved in: {save_path}")

    return model
