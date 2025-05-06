# engine/trainer.py

from engine.evaluator import evaluate_fitness

def evolve(grid, model, mutator):
    fitness = evaluate_fitness(grid.state)
    if fitness < 0.5:  # arbitrary threshold for mutation
        mutator.apply(model)
