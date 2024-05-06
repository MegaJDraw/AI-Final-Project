## create_project.bat

@echo off

mkdir sudoku_solver
cd sudoku_solver

mkdir algorithms
type nul > algorithms\__init__.py
type nul > algorithms\backtracking.py
type nul > algorithms\forward_checking.py
type nul > algorithms\arc_consistency.py

mkdir utils
type nul > utils\__init__.py
type nul > utils\sudoku_generator.py
type nul > utils\sudoku_validator.py

mkdir tests
type nul > tests\__init__.py
type nul > tests\test_backtracking.py
type nul > tests\test_forward_checking.py
type nul > tests\test_arc_consistency.py

type nul > main.py
type nul > requirements.txt

echo Project structure created successfully.

## repository.md



# sudoku_solver

## convert_to_markdown.py

import os

def should_ignore(name):
    ignore_list = [
        "__pycache__",
        "__init__.py",
        ".git",
        ".gitignore",
        ".gitattributes",
    ]
    return name in ignore_list or name.startswith(".")

def convert_directory_to_markdown(directory, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(directory):
            # Ignore specified directories
            dirs[:] = [d for d in dirs if not should_ignore(d)]

            # Write the directory path as a heading
            relative_path = os.path.relpath(root, directory)
            if relative_path != ".":
                f.write(f"# {relative_path}\n\n")

            # Write each file in the directory
            for file in files:
                if should_ignore(file):
                    continue

                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as file_content:
                        content = file_content.read()
                        f.write(f"## {file}\n\n")
                        f.write(content)
                        f.write("\n\n")
                except UnicodeDecodeError:
                    print(f"Skipping file: {file_path} (cannot decode using UTF-8)")
                    continue

# Get the current directory
current_directory = os.getcwd()

# Output file name
output_file = "repository.md"

# Convert all files in the current directory and its subdirectories to a single Markdown file
convert_directory_to_markdown(current_directory, output_file)

## gui.py

import pygame
import time

def draw_board(screen, board, solved, current_cell, insights):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)

    for i in range(9):
        for j in range(9):
            if solved[i][j]:
                color = (0, 255, 0)  # Green color for solved cells
            elif current_cell == (i, j):
                color = (255, 0, 0)  # Red color for the current cell
            else:
                color = (0, 0, 0)  # Black color for unsolved cells

            value = board[i][j]
            if value == 0:
                value = ""

            text = font.render(str(value), True, color)
            text_rect = text.get_rect()
            text_rect.center = (j * 50 + 25, i * 50 + 25)
            screen.blit(text, text_rect)

    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1

        pygame.draw.line(screen, (0, 0, 0), (i * 50, 0), (i * 50, 450), thickness)
        pygame.draw.line(screen, (0, 0, 0), (0, i * 50), (450, i * 50), thickness)

    # Display insights
    insight_font = pygame.font.Font(None, 24)
    insight_text = insight_font.render(insights, True, (0, 0, 0))
    screen.blit(insight_text, (10, 460))

    pygame.display.flip()

def is_valid(puzzle, num, pos):
    # Check row
    if num in puzzle[pos[0]]:
        return False

    # Check column
    if num in [puzzle[i][pos[1]] for i in range(9)]:
        return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    if num in [puzzle[i][j] for i in range(box_y * 3, box_y * 3 + 3) for j in range(box_x * 3, box_x * 3 + 3)]:
        return False

    return True

def visualize_solving(puzzle, algorithm):
    pygame.init()
    screen = pygame.display.set_mode((450, 500))
    pygame.display.set_caption("Sudoku Solver")

    solved = [[False] * 9 for _ in range(9)]
    current_cell = None

    # Draw the initial board
    draw_board(screen, puzzle, solved, current_cell, "")
    pygame.display.flip()

    def solve(puzzle, row, col):
        nonlocal current_cell

        if row == 9:
            print("Reached the end of the puzzle. Puzzle solved!")
            return True

        if col == 9:
            return solve(puzzle, row + 1, 0)

        if puzzle[row][col] != 0:
            solved[row][col] = True
            current_cell = (row, col)
            insights = f"Skipping cell ({row}, {col}) as it already has a value."
            print(insights)
            draw_board(screen, puzzle, solved, current_cell, insights)
            pygame.display.flip()
            pygame.time.delay(200)  # Delay between each step

            return solve(puzzle, row, col + 1)

        current_cell = (row, col)
        for num in range(1, 10):
            insights = f"Trying {num} in cell ({row}, {col})"
            print(insights)
            draw_board(screen, puzzle, solved, current_cell, insights)
            pygame.display.flip()
            pygame.time.delay(200)  # Delay between each step

            if algorithm(puzzle, num, (row, col)):
                puzzle[row][col] = num
                solved[row][col] = True
                insights = f"Placed {num} in cell ({row}, {col})"
                print(insights)
                draw_board(screen, puzzle, solved, current_cell, insights)
                pygame.display.flip()
                pygame.time.delay(200)  # Delay between each step

                if solve(puzzle, row, col + 1):
                    return True

                puzzle[row][col] = 0
                solved[row][col] = False
                insights = f"Backtracking from cell ({row}, {col})"
                print(insights)
                draw_board(screen, puzzle, solved, current_cell, insights)
                pygame.display.flip()
                pygame.time.delay(200)  # Delay between each step

        current_cell = None
        print(f"No valid value found for cell ({row}, {col}). Backtracking.")
        return False

    clock = pygame.time.Clock()

    while True:
        clock.tick(30)  # Limit the frame rate to 30 FPS

        try:
            if solve(puzzle, 0, 0):
                insights = "Sudoku solved!"
                print(insights)
                draw_board(screen, puzzle, solved, current_cell, insights)
                pygame.display.flip()
                time.sleep(2)  # Pause for 2 seconds before closing the window
                break
        except ValueError as e:
            print("Error during solving:", str(e))
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    pygame.quit()

## main.py

from sudoku_solver.algorithms.backtracking import backtracking
from sudoku_solver.algorithms.forward_checking import forward_checking
from sudoku_solver.algorithms.arc_consistency import arc_consistency
from sudoku_solver.utils.sudoku_generator import generate_sudoku
from sudoku_solver.gui import visualize_solving

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
            visualize_solving(puzzle, algorithm)
            print()

        print()

if __name__ == '__main__':
    main()

## requirements.txt



# sudoku_solver\algorithms

## arc_consistency.py

def arc_consistency(puzzle, num, pos):
    row, col = pos

    # Check if the number is valid at the given position
    if not is_valid(puzzle, num, pos):
        return False

    # Assign the number to the cell
    puzzle[row][col] = num

    # Check if the puzzle is solved
    if find_empty(puzzle) is None:
        return True

    # Recursive call to solve the next empty cell
    find = find_empty(puzzle)
    if find:
        row, col = find
        for i in range(1, 10):
            if arc_consistency(puzzle, i, (row, col)):
                return True

    # Backtrack if the current number doesn't lead to a solution
    puzzle[row][col] = 0
    return False

def find_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None

def is_valid(puzzle, num, pos):
    # Check row
    for i in range(9):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False

    return True

## backtracking.py

def backtracking(puzzle, num, pos):
    row, col = pos

    # Check if the number is valid at the given position
    if not is_valid(puzzle, num, pos):
        return False

    # Assign the number to the cell
    puzzle[row][col] = num

    # Check if the puzzle is solved
    if find_empty(puzzle) is None:
        return True

    # Recursive call to solve the next empty cell
    find = find_empty(puzzle)
    if find:
        row, col = find
        for i in range(1, 10):
            if backtracking(puzzle, i, (row, col)):
                return True

    # Backtrack if the current number doesn't lead to a solution
    puzzle[row][col] = 0
    return False

def find_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None

def is_valid(puzzle, num, pos):
    # Check row
    for i in range(9):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False

    return True

## forward_checking.py

def forward_checking(puzzle, num, pos):
    row, col = pos

    # Check if the number is valid at the given position
    if not is_valid(puzzle, num, pos):
        return False

    # Assign the number to the cell
    puzzle[row][col] = num

    # Check if the puzzle is solved
    if find_empty(puzzle) is None:
        return True

    # Recursive call to solve the next empty cell
    find = find_empty(puzzle)
    if find:
        row, col = find
        for i in range(1, 10):
            if forward_checking(puzzle, i, (row, col)):
                return True

    # Backtrack if the current number doesn't lead to a solution
    puzzle[row][col] = 0
    return False

def find_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None

def is_valid(puzzle, num, pos):
    # Check row
    for i in range(9):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i, j) != pos:
                return False

    return True

# sudoku_solver\tests

## test_arc_consistency.py

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

## test_backtracking.py

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

## test_forward_checking.py

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

# sudoku_solver\utils

## sudoku_generator.py

import random

def generate_sudoku(difficulty):
    # Initialize an empty 9x9 grid
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Fill the diagonal 3x3 boxes with random numbers
    for i in range(0, 9, 3):
        fill_box(grid, i, i)

    # Solve the grid to ensure it has a valid solution
    solve(grid)

    # Remove numbers based on the difficulty level
    remove_numbers(grid, difficulty)

    return grid

def fill_box(grid, row, col):
    nums = list(range(1, 10))
    random.shuffle(nums)

    for i in range(3):
        for j in range(3):
            grid[row + i][col + j] = nums[i * 3 + j]

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, num, pos):
    # Check row
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False

def remove_numbers(grid, difficulty):
    count = 0
    while count < difficulty:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if grid[row][col] != 0:
            grid[row][col] = 0
            count += 1

## sudoku_validator.py

def is_valid_solution(puzzle):
    # Check rows
    for row in puzzle:
        if not is_valid_unit(row):
            return False

    # Check columns
    for col in zip(*puzzle):
        if not is_valid_unit(col):
            return False

    # Check boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [puzzle[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(box):
                return False

    return True

def is_valid_unit(unit):
    return set(unit) == set(range(1, 10))

