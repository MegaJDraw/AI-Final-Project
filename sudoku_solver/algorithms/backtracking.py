def backtracking(puzzle):
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

    def solve(puzzle):
        find = find_empty(puzzle)
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if is_valid(puzzle, num, (row, col)):
                puzzle[row][col] = num

                if solve(puzzle):
                    return True

                puzzle[row][col] = 0

        return False

    solve(puzzle)
    return puzzle
