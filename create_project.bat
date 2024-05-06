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