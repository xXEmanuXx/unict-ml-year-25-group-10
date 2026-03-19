import torch
from torch import nn
import os

class DeepMLP(nn.Module):
    def __init__(self, in_features, hidden_units, out_features):
        super().__init__()
        
        layers = []
        input_dim = in_features

        for hidden_dim in hidden_units:
            layers.append(nn.Linear(input_dim, hidden_dim))
            layers.append(nn.ReLU())
            input_dim = hidden_dim

        layers.append(nn.Linear(input_dim, out_features))

        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)
    
def load_model(model, path, device):
    if os.path.exists(path):
        model.load_state_dict(torch.load(path, map_location=device))
        model.to(device)

        print(f"Model loaded from: {path}")

        return model, True
    else:
        return model, False

def predict(model, mean, std, device, features):
    x = torch.tensor([features], dtype=torch.float32)
    x = (x - mean) / std

    model.eval()
    with torch.no_grad():
        logits = model(x.to(device))
        probs = torch.softmax(logits, dim=1)

    prob = probs[0][1].item()
    pred = logits.argmax(dim=1).item()

    return pred, prob