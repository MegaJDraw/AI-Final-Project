import unittest
from sudoku_solver.algorithms.forward_checking import forward_checking
from sudoku_solver.utils.sudoku_generator import generate_sudoku
from sudoku_solver.utils.sudoku_validator import is_valid_solution

class TestForwardChecking(unittest.TestCase):
    def test_forward_checking(self):
        # Generate Sudoku puzzles of different difficulty levels
        easy_puzzle = generate_sudoku(30)
        medium_puzzle = generate_sudoku(40)
        hard_puzzle = generate_sudoku(50)

        # Solve the puzzles using forward checking
        easy_solution = forward_checking(easy_puzzle)
        medium_solution = forward_checking(medium_puzzle)
        hard_solution = forward_checking(hard_puzzle)

        # Check if the solutions are valid
        self.assertTrue(is_valid_solution(easy_solution))
        self.assertTrue(is_valid_solution(medium_solution))
        self.assertTrue(is_valid_solution(hard_solution))

if __name__ == '__main__':
    unittest.main()
