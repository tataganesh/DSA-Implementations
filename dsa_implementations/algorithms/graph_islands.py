from collections import deque


def depth_first_traversal(grid, row, col, num_rows, num_cols, visited) -> bool:
    # Check if neighbour is out-of-bounds
    if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
        return False
    # If cell has been visited, then no need to do further traversal
    if (row, col) in visited:
        return False
    # If reached here, we have visited a new cell/node.
    ## Only perform further traversal if the current cell
    ## is land, since we do NOT want to hit or traverse
    ## further from a water cell
    if grid[row][col] == "W":
        return False
    visited.add((row, col))
    # Now, do depth-first traversal of each neighbour
    depth_first_traversal(grid, row - 1, col, num_rows, num_cols, visited)
    depth_first_traversal(grid, row, col + 1, num_rows, num_cols, visited)
    depth_first_traversal(grid, row + 1, col, num_rows, num_cols, visited)
    depth_first_traversal(grid, row, col - 1, num_rows, num_cols, visited)
    return True


def breadth_first_traversal(grid, row, col, num_rows, num_cols, visited):
    queue = deque()
    queue.append((row, col))
    visited.add((row, col))
    while len(queue):
        current_row, current_col = queue.pop()
        candidate_neighbours = [
            (current_row - 1, current_col),
            (current_row + 1, current_col),
            (current_row, current_col - 1),
            (current_row, current_col + 1),
        ]
        for c_row, c_col in candidate_neighbours:
            ## skip if out-of-bounds
            if c_row < 0 or c_col < 0 or c_row >= num_rows or c_col >= num_cols:
                continue
            ## Only add unvisited "land" cells to the queue for further breath-first-traversal
            if (c_row, c_col) not in visited and grid[c_row][c_col] == "L":
                visited.add((c_row, c_col))
                queue.append((c_row, c_col))


def island_count(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    count = 0
    visited = set()
    for row in range(num_rows):
        for col in range(num_cols):
            # Perform depth-first traversal
            found_island = depth_first_traversal(
                grid, row, col, num_rows, num_cols, visited
            )
            if found_island:
                count += 1
    return count


if __name__ == "__main__":
    grid = [
        ["W", "L", "W", "W", "W"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "L", "W"],
        ["W", "W", "L", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "W"],
    ]
    print(island_count(grid))
