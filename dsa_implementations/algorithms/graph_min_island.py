import sys


def count_cells(grid, row, col, visited) -> int:
    ## out-of-bounds check
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return 0
    ## if visited, return 0
    if (row, col) in visited:
        return 0
    ## no cells further if current cell is water
    if grid[row][col] == "W":
        return 0
    ## Found a land cell! We could that as one cell
    ## and add it to visited
    count = 1
    visited.add((row, col))

    ## Now do depth first traversal starting from
    ## neighboring nodes and get their counts
    ## Here, neighbors are up-down-left-right
    count += count_cells(grid, row - 1, col, visited)
    count += count_cells(grid, row + 1, col, visited)
    count += count_cells(grid, row, col - 1, visited)
    count += count_cells(grid, row, col + 1, visited)
    return count


def minimum_island(grid) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    visited: set[str] = set()
    # Assigning sys.maxsize ensures LARGE min value
    # when starting
    min_count = sys.maxsize

    # go through each cell of grid.
    # Assume each cell is a node of a graph
    for row in range(num_rows):
        for col in range(num_cols):
            # Count cells in the current island.
            # Note: If cell has been visited OR if
            # it is a water cell, cell_count will be
            # 0 and it will NOT be considered for updating
            # minimum (as seen by the condition below).
            # This way, all conditions are handled by the
            # recursive depth-first traversal
            cell_count = count_cells(grid, row, col, visited)
            if cell_count:
                min_count = min(min_count, cell_count)
    return min_count


if __name__ == "__main__":
    grid = [
        ["W", "L", "W", "W", "W"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "L", "W"],
        ["W", "W", "L", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "W"],
    ]

    print(minimum_island(grid))  # -> 2
