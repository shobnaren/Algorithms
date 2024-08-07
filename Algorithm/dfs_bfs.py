"""
DFS :
- use stack
- start with the current node
- push it into stack

    - pop the stack
    - check if it's the goal
    push the neighbor
    add the predecessor , neighbor => current
    repeat the step
"""
from helper import is_legal, offsets, get_path, read_maze
from queue_handson import Queue
from stack import Stack


def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}
    while not stack.is_empty():
        current_node = stack.pop()
        if current_node == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_off, col_off = offsets[direction]
            neighbor = (current_node[0] + row_off, current_node[1] + col_off)
            if is_legal(maze, neighbor) and neighbor not in predecessors:
                # push the neighbor into stack
                stack.push(neighbor)
                # add the predecessors for the neighbor
                predecessors[neighbor] = current_node
    return None


def bfs(maze, start, goal):
    # similar to dfs but it uses queue instead of stack
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}
    while not queue.is_empty():
        current_cell = queue.dequeue()
        if goal == current_cell:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_off, col_off = offsets[direction]
            neighbor = (current_cell[0] + row_off, current_cell[1] + col_off)
            if is_legal(maze, neighbor) and neighbor not in predecessors:
                # push the neighbor into stack
                queue.enqueue(neighbor)
                # add the predecessors for the neighbor
                predecessors[neighbor] = current_cell
    return None


if __name__ == "__main__":
    # # Test 1
    # maze = [[0] * 3 for row in range(3)]
    # print(maze)
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    #
    # # Test 2
    # maze = read_maze("mazes/mini_maze_dfs.txt")
    # for row in maze:
    #     print(row)
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = dfs(maze, start_pos, goal_pos)
    # assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    #
    # # Test 3
    # maze = read_maze("mazes/mini_maze_dfs.txt")
    # start_pos = (0, 0)
    # goal_pos = (3, 3)
    # result = dfs(maze, start_pos, goal_pos)
    # assert result is None

    # maze = read_maze("mazes/new_maze.txt")
    # print(maze)
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # maze = read_maze("mazes/challenge_maze.txt")
    # print(maze)
    # start_pos = (0, 0)
    # goal_pos = (3, 3)
    # result = dfs(maze, start_pos, goal_pos)
    # print(result)
    # assert result == [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]

    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    print(result)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # # Test 2
    # maze = read_maze("DataStructure/Ex_Files_Python_Data_Structures/Exercise Files/06_03_begin/mazes/mini_maze_bfs.txt")
    # # for row in maze:
    # #     print(row)
    # start_pos = (0, 0)
    # goal_pos = (2, 2)
    # result = bfs(maze, start_pos, goal_pos)
    # assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # # Test 3
    # maze = read_maze("DataStructure/Ex_Files_Python_Data_Structures/Exercise Files/06_03_begin/mazes/mini_maze_bfs.txt")
    # start_pos = (0, 0)
    # goal_pos = (3, 3)
    # result = bfs(maze, start_pos, goal_pos)
    # assert result is None
