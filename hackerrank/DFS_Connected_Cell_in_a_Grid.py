'''
DFS: Connected Cell in a Grid

'''


def getBiggestRegion(grid):
    maxRegion = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxRegion = max(maxRegion, countCells(grid, i, j))
    return maxRegion


def countCells(grid, i, j):
    if (not (i in range(len(grid)) and j in range(len(grid[0])))):
        return 0
    if (grid[i][j] == 0):
        return 0
    count = 1
    grid[i][j] = 0
    count += countCells(grid, i + 1, j)
    count += countCells(grid, i - 1, j)
    count += countCells(grid, i, j + 1)
    count += countCells(grid, i, j - 1)
    count += countCells(grid, i + 1, j + 1)
    count += countCells(grid, i - 1, j - 1)
    count += countCells(grid, i - 1, j + 1)
    count += countCells(grid, i + 1, j - 1)
    return count


def get_region(row, col, grid):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return 0
    if grid[row][col] == 0:
        return 0
    reg = 1
    grid[row][col] = 0
    reg += get_region(row + 1, col, grid)
    reg += get_region(row - 1, col, grid)
    reg += get_region(row, col + 1, grid)
    reg += get_region(row, col - 1, grid)
    reg += get_region(row + 1, col + 1, grid)
    reg += get_region(row - 1, col - 1, grid)
    reg += get_region(row + 1, col - 1, grid)
    reg += get_region(row - 1, col + 1, grid)

    return reg


def get_biggest_region(grid):
    max_reg = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            max_reg = max(max_reg, get_region(row, col, grid))
    return max_reg


# grid = [[1, 0, 1], [0, 1, 0], [0, 1, 0]]
grid = [[1, 0], [0, 1]]

print get_biggest_region(grid)
