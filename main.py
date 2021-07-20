def is_valid_move(grid_array, row, col, number):
    for x in range(9):
        if grid_array[row][x] == number:
            return False

    for x in range(9):
        if grid_array[x][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if grid_array[corner_row + x][corner_col + y] == number:
                return False

    return True


def solve(grid_array, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid_array[row][col] > 0:
        return solve(grid_array, row, col + 1)

    for num in range(1, 10):
        if is_valid_move(grid_array, row, col, num):
            grid_array[row][col] = num

            if solve(grid_array, row, col + 1):
                return True

        grid_array[row][col] = 0
    return False


if __name__ == '__main__':

    grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
            [0, 0, 0, 0, 7, 3, 0, 0, 9],
            [3, 0, 9, 0, 0, 0, 0, 4, 5],
            [4, 9, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 3, 0, 5, 0, 9, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 3, 6],
            [9, 6, 0, 0, 0, 0, 3, 0, 8],
            [7, 0, 0, 6, 8, 0, 0, 0, 0],
            [0, 2, 8, 0, 0, 0, 0, 0, 0]]

    if solve(grid, 0, 0):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")
            print()
    else:
        print("No solution for this sudoku")
