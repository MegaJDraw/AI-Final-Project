import unittest
from sudoku_solver.algorithms.backtracking import backtracking
from sudoku_solver.utils.sudoku_generator import generate_sudoku
from sudoku_solver.utils.sudoku_validator import is_valid_solution

class TestBacktracking(unittest.TestCase):
    def test_backtracking(self):
        # Generate a Sudoku puzzle
        puzzle = generate_sudoku(30)

        # Solve the puzzle using backtracking
        solution = backtracking(puzzle)

        # Check if the solution is valid
        self.assertTrue(is_valid_solution(solution))

if __name__ == '__main__':
    unittest.main()