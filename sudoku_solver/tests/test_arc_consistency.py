import unittest
from sudoku_solver.algorithms.arc_consistency import arc_consistency
from sudoku_solver.utils.sudoku_generator import generate_sudoku
from sudoku_solver.utils.sudoku_validator import is_valid_solution

class TestArcConsistency(unittest.TestCase):
    def test_arc_consistency(self):
        # Generate a Sudoku puzzle
        puzzle = generate_sudoku(30)

        # Solve the puzzle using arc consistency
        solution = arc_consistency(puzzle)

        # Check if the solution is valid
        self.assertTrue(is_valid_solution(solution))

if __name__ == '__main__':
    unittest.main()