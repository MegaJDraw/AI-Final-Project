from sudoku_solver.algorithms.backtracking import backtracking
from sudoku_solver.algorithms.forward_checking import forward_checking
from sudoku_solver.algorithms.arc_consistency import arc_consistency
from sudoku_solver.utils.sudoku_generator import generate_sudoku
from sudoku_solver.gui import visualize_solving

import time

def main():
    # Generate Sudoku puzzles of different difficulty levels
    easy_puzzle = generate_sudoku(30)
    medium_puzzle = generate_sudoku(40)
    hard_puzzle = generate_sudoku(50)

    # Solve the puzzles using different algorithms and visualize the solving process
    algorithms = [backtracking, forward_checking, arc_consistency]
    puzzles = [easy_puzzle, medium_puzzle, hard_puzzle]
    difficulty_labels = ['Easy', 'Medium', 'Hard']

    for i, puzzle in enumerate(puzzles):
        print(f"Puzzle Difficulty: {difficulty_labels[i]}")
        for algorithm in algorithms:
            print(f"Algorithm: {algorithm.__name__}")
            start_time = time.time()
            solution, explored_nodes = algorithm(puzzle)
            end_time = time.time()
            solving_time = end_time - start_time
            print(f"Solving Time: {solving_time:.3f} seconds")
            print(f"Explored Nodes: {explored_nodes}")
            visualize_solving(puzzle, algorithm)
            print()

        print()

if __name__ == '__main__':
    main()
