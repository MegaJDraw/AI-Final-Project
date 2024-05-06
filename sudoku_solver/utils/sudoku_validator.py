def is_valid_solution(puzzle):
    # Check rows
    for i, row in enumerate(puzzle):
        if not is_valid_unit(row):
            print(f"Invalid row: {i}")
            return False

    # Check columns
    for j, col in enumerate(zip(*puzzle)):
        if not is_valid_unit(col):
            print(f"Invalid column: {j}")
            return False

    # Check boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [puzzle[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(box):
                print(f"Invalid box: ({i}, {j})")
                return False

    return True

def is_valid_unit(unit):
    return sorted(unit) == list(range(1, 10))
