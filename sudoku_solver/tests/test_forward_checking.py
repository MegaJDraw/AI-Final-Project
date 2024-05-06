import unittest
from sudoku_solver.algorithms.forward_checking import forward_checking
from sudoku_solver.utils.sudoku_generator import generate_sudoku
from sudoku_solver.utils.sudoku_validator import is_valid_solution

class TestForwardChecking(unittest.TestCase):
    def test_forward_checking(self):
        # Generate a Sudoku puzzle
        puzzle = generate_sudoku(30)

        # Solve the puzzle using forward checking
        solution = forward_checking(puzzle)

        # Check if the solution is valid
        self.assertTrue(is_valid_solution(solution))

if __name__ == '__main__':
    unittest.main()