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