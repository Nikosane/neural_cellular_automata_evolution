# config.py

# Global Configuration and Hyperparameters

GRID_SIZE = (32, 32)            # Width x Height
CHANNELS = 16                   # Number of state channels per cell
EVOLUTION_STEPS = 1000         # Number of evolution steps per run
MUTATION_RATE = 0.05           # Rate of mutation per rule update
SEED_PATTERN = 'glider'        # Initial pattern loaded from assets
FITNESS_TARGET = 'growth'      # Options: 'growth', 'stability', 'complexity'

NEURAL_ARCHITECTURE = {
    'layers': [
        {'type': 'conv', 'out_channels': 32, 'kernel_size': 3},
        {'type': 'relu'},
        {'type': 'conv', 'out_channels': CHANNELS, 'kernel_size': 1}
    ]
}
