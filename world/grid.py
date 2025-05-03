# world/grid.py

import numpy as np
from config import CHANNELS

class Grid:
    def __init__(self, size):
        self.width, self.height = size
        self.state = np.random.rand(self.height, self.width, CHANNELS).astype(np.float32)

    def get_neighborhood(self, x, y, radius=1):
        x0 = max(x - radius, 0)
        x1 = min(x + radius + 1, self.width)
        y0 = max(y - radius, 0)
        y1 = min(y + radius + 1, self.height)
        return self.state[y0:y1, x0:x1, :]

    def update(self, cell_model):
        new_state = np.zeros_like(self.state)
        for y in range(self.height):
            for x in range(self.width):
                neighborhood = self.get_neighborhood(x, y)
                new_state[y, x] = cell_model.predict(neighborhood)
        self.state = new_state

