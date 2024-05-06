# Sudoku Solver

This project implements three constraint satisfaction algorithms—backtracking search, forward checking, and arc consistency—for solving Sudoku puzzles. The algorithms are implemented in Python and evaluated on Sudoku puzzles of varying difficulty levels.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/sudoku-solver.git
   ```

2. Navigate to the project directory:
   ```
   cd sudoku-solver
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to solve Sudoku puzzles:
   ```
   python main.py
   ```

2. The script will generate Sudoku puzzles of different difficulty levels (easy, medium, hard) and solve them using the three constraint satisfaction algorithms.

3. The solving times and the number of explored nodes for each algorithm will be displayed in the console.

4. To visualize the solving process, run the GUI script:
   ```
   python gui.py
   ```

5. The GUI will display the Sudoku grid and allow you to step through the solving process for each algorithm.

## Algorithms

The project implements three constraint satisfaction algorithms for solving Sudoku puzzles:

1. **Backtracking Search**: A fundamental algorithm that systematically explores the search space by incrementally building a solution and backtracking when a constraint violation is encountered.

2. **Forward Checking**: An extension of backtracking search that maintains arc consistency for the unassigned variables, pruning the search space by removing inconsistent values.

3. **Arc Consistency**: A more advanced technique that ensures consistency between pairs of variables, further reducing the search space.

## Visualization

The project includes a graphical user interface (GUI) for visualizing the solving process of the algorithms. The GUI is implemented using the Pygame library and allows users to step through the solving process, observing the assignment of values to cells, the backtracking process, and the consistency checks performed.

To run the GUI, execute the `gui.py` script:
```
python gui.py
```

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes.
