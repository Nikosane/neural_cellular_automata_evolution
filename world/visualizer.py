# world/visualizer.py

import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.img = None

    def render(self, state, step):
        grayscale = np.mean(state, axis=2)
        if self.img is None:
            self.img = self.ax.imshow(grayscale, cmap='viridis', interpolation='nearest')
        else:
            self.img.set_data(grayscale)
        self.ax.set_title(f"Step {step}")
        plt.pause(0.01)
