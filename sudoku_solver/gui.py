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