import unittest
from sudoku_solver.algorithms.arc_consistency import arc_consistency
from sudoku_solver.utils.sudoku_generator import generate_sudoku
from sudoku_solver.utils.sudoku_validator import is_valid_solution

class TestArcConsistency(unittest.TestCase):
    def test_arc_consistency(self):
        # Generate Sudoku puzzles of different difficulty levels
        easy_puzzle = generate_sudoku(30)
        medium_puzzle = generate_sudoku(40)
        hard_puzzle = generate_sudoku(50)

        # Solve the puzzles using arc consistency
        easy_solution = arc_consistency(easy_puzzle)
        medium_solution = arc_consistency(medium_puzzle)
        hard_solution = arc_consistency(hard_puzzle)

        # Check if the solutions are valid
        self.assertTrue(is_valid_solution(easy_solution))
        self.assertTrue(is_valid_solution(medium_solution))
        self.assertTrue(is_valid_solution(hard_solution))

if __name__ == '__main__':
    unittest.main()
