# write agnostic helper methods for DFS & BFS

def read_maze(filename):
    matrix = []
    with open(filename) as fh:
        lines = fh.readlines()
    for line in lines:
        matrix.append([ch for ch in line])
    return matrix


# define offsets for the directions
offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


# check legal move
def is_legal(maze: list, pos: tuple):
    # check the maze doesn't have '*' in the current position
    row, col = pos
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != '*'


def get_path(predecessors, start, goal):
    # get the path from the predecessors from start to goal
    print('pred:', predecessors)
    current = goal
    path = []
    while current != start:
        # update the current in path list
        path.append(current)
        current = predecessors[current]
    path.append(start)
    print('path:',path)
    path.reverse()
    return path  # back track the path by reversing the list
