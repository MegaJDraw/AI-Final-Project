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