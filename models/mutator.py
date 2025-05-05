# models/mutator.py

class Mutator:
    def __init__(self, mutation_rate=0.05):
        self.mutation_rate = mutation_rate

    def apply(self, model):
        model.mutate(self.mutation_rate)
