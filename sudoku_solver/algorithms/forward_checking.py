def forward_checking(puzzle):
    explored_nodes = 0

    def find_empty(puzzle):
        nonlocal explored_nodes
        explored_nodes += 1
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return i, j
        return None

    def is_valid(puzzle, num, pos):
        nonlocal explored_nodes
        explored_nodes += 1
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

    def get_candidates(puzzle, pos):
        nonlocal explored_nodes
        explored_nodes += 1
        candidates = set(range(1, 10))

        # Remove numbers in the same row
        candidates -= set(puzzle[pos[0]])

        # Remove numbers in the same column
        candidates -= set(puzzle[i][pos[1]] for i in range(9))

        # Remove numbers in the same box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        candidates -= set(puzzle[i][j] for i in range(box_y * 3, box_y * 3 + 3) for j in range(box_x * 3, box_x * 3 + 3))

        return candidates

    def solve(puzzle):
        find = find_empty(puzzle)
        if not find:
            return True
        else:
            row, col = find

        candidates = get_candidates(puzzle, (row, col))

        for num in candidates:
            if is_valid(puzzle, num, (row, col)):
                puzzle[row][col] = num

                if solve(puzzle):
                    return True

                puzzle[row][col] = 0

        return False

    if solve(puzzle):
        return puzzle, explored_nodes
    else:
        return None, explored_nodes
