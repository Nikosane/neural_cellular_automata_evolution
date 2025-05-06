# engine/evaluator.py

import numpy as np

def evaluate_fitness(state):
    # Simple fitness function: how much of the grid is active
    activity = np.mean(state)
    return activity
