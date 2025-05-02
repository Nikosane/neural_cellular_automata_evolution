# 🧬 Neural Cellular Automata Evolution

**Neural Cellular Automata Evolution** is an experimental simulation where neural networks evolve not only the state of each cell in a grid (like Conway's Game of Life) but also learn and mutate the *laws of nature*—i.e., the update rules themselves. This is an artificial life simulator where emergent behavior, pattern formation, and rule evolution all come together in a self-organizing system.

---

## 🚀 Key Features

* **Neural Cell Update Rules**: Each cell uses a neural network (MLP or CNN) to determine its next state based on its local neighborhood.
* **Evolving Rules**: The weights of the neural networks mutate over time using evolutionary strategies.
* **Fitness-Based Training**: Cells or populations are rewarded based on customizable objectives like pattern complexity, growth, or persistence.
* **Dynamic Laws of Nature**: Mutators themselves can evolve, allowing the rules of mutation to be learned.
* **Interactive Visualization**: Watch how the cellular universe changes over time.

---

## 🧠 Concept Overview

Traditional Cellular Automata like Conway’s Game of Life have hardcoded rules. Here, each cell learns its own rules with a neural network and evolves those rules over time.

**How it works:**

1. Each cell gets a local neighborhood as input.
2. A small neural network outputs the new state.
3. Mutation applies changes to the weights (random noise, crossover, etc.).
4. The grid updates in parallel.
5. The system evaluates fitness to determine which rule sets survive.
6. Repeat — evolution unfolds.

---

## ⚙️ Installation

### 🔧 Prerequisites

* Python 3.9+
* pip

### 📦 Setup

```bash
git clone https://github.com/Nikosane/neural_cellular_automata_evolution.git
cd neural_cellular_automata_evolution
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main simulation:

```bash
python main.py
```

Visualize live cellular evolution in the terminal or a pop-up window (depending on backend).

---

## ⚙️ Configuration

Modify `config.py` to:

* Change grid size
* Set number of channels
* Tweak mutation rates
* Choose neural network architecture
* Customize fitness functions

---

## 🧚️‍ Experiments You Can Try

* Stability vs. Chaos: Try maximizing entropy or minimizing change.
* Pattern Seeding: Start from simple seeds and let the system build complexity.
* Evolutionary Pressure: Evolve to replicate or spread across the grid.
* Species Coexistence: Compete multiple rule-sets across the same grid.

---

## 📊 Example Fitness Metrics

* Average survival time of active cells
* Number of distinct patterns over time
* Growth rate (spread vs. stability)
* Symmetry or entropy of the grid
* Replication or motion-like behaviors

---

## 💡 Inspiration

* [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
* [Neural Cellular Automata (Google Research)](https://distill.pub/2020/growing-ca/)
* Evolutionary Computation and Artificial Life

---

## 🛠️ Built With

* Python
* NumPy / PyTorch / TensorFlow (optional)
* Matplotlib / OpenCV for visualization

---

## 📂 Future Roadmap

* [ ] Save & Load rule sets (weights)
* [ ] GUI-based visualizer
* [ ] Competitive multi-species CA
* [ ] Integration with Reinforcement Learning
* [ ] Memory-augmented neural cells

---

## 🤝 Contribution

Want to explore emergent life? Fork this repo, try new mutation strategies, or invent new kinds of cells! PRs and ideas welcome.
