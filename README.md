# Prey vs Predator Simulation

This project simulates a prey vs predator environment using Proximal Policy Optimization (PPO) algorithm for training the agents. The simulation involves prey and predator entities interacting in a 2D grid environment.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/prey-predator-simulation.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the simulation, execute the following command:
```
python -m src.main
```

This will start the training process for the prey and predator agents using PPO. After training, the simulation will be visualized, and the performance metrics and best genes will be analyzed.

## Project Structure

The project structure is as follows:

```
prey-predator-simulation/
│
├── src/
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── entity.py
│   │   ├── prey.py
│   │   └── predator.py
│   │
│   ├── algorithms/
│   │   ├── __init__.py
│   │   └── ppo.py
│   │
│   ├── environment/
│   │   ├── __init__.py
│   │   └── simulation.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── visualization.py
│   │   └── analysis.py
│   │
│   └── main.py
│
├── models/
│   ├── prey/
│   └── predator/
│
├── data/
│   ├── benchmarks/
│   └── best_genes/
│
├── results/
│   ├── visualizations/
│   └── animations/
│
├── tests/
│   ├── __init__.py
│   ├── test_entities.py
│   ├── test_ppo.py
│   └── test_simulation.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

- `src/`: Contains the main source code of the project.
  - `entities/`: Implements the prey and predator entities.
  - `algorithms/`: Implements the PPO algorithm for training the agents.
  - `environment/`: Implements the simulation environment.
  - `utils/`: Contains utility modules for visualization and analysis.
  - `main.py`: The main entry point of the program.

- `models/`: Stores the trained models for prey and predator agents.
- `data/`: Contains the data generated during the simulation.
- `results/`: Stores the generated results, including visualizations and animations.
- `tests/`: Contains the unit tests for different components of the project.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: Provides an overview of the project and instructions for running the simulation.
- `LICENSE`: Specifies the license under which the project is distributed.

## License

This project is licensed under the [MIT License](LICENSE).