import torch

print(torch.backends.mps.is_available()) # MacOS > 12.3+
print(torch.backends.mps.is_built()) # MPS is activated

device = 'mps' if torch.backends.mps.is_available() else 'cpu'
print(device)