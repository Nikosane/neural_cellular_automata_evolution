# models/automata_cell.py

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from config import CHANNELS

class NeuralCell(nn.Module):
    def __init__(self):
        super(NeuralCell, self).__init__()
        self.conv1 = nn.Conv2d(CHANNELS, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, CHANNELS, kernel_size=1)

    def forward(self, neighborhood):
        # neighborhood: [H, W, C] -> [1, C, H, W]
        x = torch.tensor(neighborhood, dtype=torch.float32).permute(2, 0, 1).unsqueeze(0)
        x = F.relu(self.conv1(x))
        x = self.conv2(x)
        return x.squeeze(0).permute(1, 2, 0).detach().numpy()[1, 1]  # Return center pixel

    def predict(self, neighborhood):
        return self.forward(neighborhood)

    def mutate(self, mutation_rate=0.05):
        with torch.no_grad():
            for param in self.parameters():
                noise = torch.randn_like(param) * mutation_rate
                param.add_(noise)
