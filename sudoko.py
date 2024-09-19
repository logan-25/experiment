import random

# Helper function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(row)

# Function to check if the number is safe to place in the current cell
def is_safe(grid, row, col, num):
    # Check if the number is already in the row
    if num in grid[row]:
        return False

    # Check if the number is already in the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number is in the 3x3 subgrid
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve Sudoku using backtracking
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num  # Place the number

                        if solve_sudoku(grid):  # Recursively try to solve the rest of the grid
                            return True

                        grid[row][col] = 0  # Reset if it doesn't work
                return False  # No valid number found, trigger backtracking
    return True  # Solved!

# Function to generate a randomized Sudoku puzzle
def generate_random_sudoku():
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Place some random numbers to start the puzzle
    for _ in range(20):  # Randomly fill 20 cells
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if is_safe(grid, row, col, num):
            grid[row][col] = num

    return grid

# Generate a random Sudoku puzzle
random_sudoku = generate_random_sudoku()

print("Random Sudoku Puzzle:")
print_grid(random_sudoku)

# Try to solve the puzzle
if solve_sudoku(random_sudoku):
    print("\nSolved Sudoku Puzzle:")
    print_grid(random_sudoku)
else:
    print("No solution exists.")
