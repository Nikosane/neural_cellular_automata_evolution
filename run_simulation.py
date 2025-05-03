# run_simulation.py

from world.grid import Grid
from world.visualizer import Visualizer
from models.automata_cell import NeuralCell
from models.mutator import Mutator
from engine.trainer import evolve
from config import GRID_SIZE, EVOLUTION_STEPS

def run():
    grid = Grid(GRID_SIZE)
    visualizer = Visualizer()
    cell_model = NeuralCell()
    mutator = Mutator()

    for step in range(EVOLUTION_STEPS):
        grid.update(cell_model)
        visualizer.render(grid.state, step)
        evolve(grid, cell_model, mutator)

    print("\nSimulation completed.")
