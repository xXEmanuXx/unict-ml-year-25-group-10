import torch
from torch import nn
from torch.optim import SGD
import os
from sklearn.metrics import accuracy_score

def train_model(model, train_loader, test_loader, device, save_path, lr=0.05, epochs=300):
    model = model.to(device)

    weights = torch.tensor([1.0, 2.0]).to(device)
    criterion = nn.CrossEntropyLoss(weight=weights)
    optimizer = SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=0.001)

    for epoch in range(epochs):
        model.train()

        train_loss = 0.0
        y_true = []
        y_pred = []
        
        for X_batch, Y_batch in train_loader:
            X_batch = X_batch.to(device)
            Y_batch = Y_batch.to(device)

            output = model(X_batch)
            loss = criterion(output, Y_batch)

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            train_loss += loss.item() * X_batch.size(0)

            preds = output.argmax(dim=1) 
            y_true.extend(Y_batch.cpu().numpy())
            y_pred.extend(preds.cpu().numpy())

        train_loss /= len(train_loader.dataset)
        train_acc = accuracy_score(y_true, y_pred)

        model.eval()

        test_loss = 0.0
        y_true = []
        y_pred = []

        with torch.no_grad():
            for X_batch, Y_batch in test_loader:
                X_batch = X_batch.to(device)
                Y_batch = Y_batch.to(device)

                output = model(X_batch)

                loss = criterion(output, Y_batch)
                test_loss += loss.item() * X_batch.size(0)
                
                preds = output.argmax(dim=1)
                y_true.extend(Y_batch.cpu().numpy())
                y_pred.extend(preds.cpu().numpy())

        test_loss /= len(test_loader.dataset)
        test_acc = accuracy_score(y_true, y_pred)

        if epoch % 50 == 0:
            print(f"Epoch {epoch+1}/{epochs} complete")

    print(f"Epoch {epoch+1}/{epochs} complete\n")

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    torch.save(model.state_dict(), save_path)

    print(f"Model saved in: {save_path}")

    return model