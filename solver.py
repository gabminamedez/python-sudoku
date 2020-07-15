def isPossible(grid, pos, num):
    row = pos[0]
    col = pos[1]

    for i in range(9):
        if grid[row][i] == num:
            return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    rowDiv = (row // 3) * 3
    colDiv = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[rowDiv + i][colDiv + j] == num:
                return False

    return True

def findEmpty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)

    return None

def solve(grid):
    empty = findEmpty(grid)

    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if isPossible(grid, (row, col), num):
            grid[row][col] = num

        if solve(grid):
            return True

        grid[row][col] == 0

    return False