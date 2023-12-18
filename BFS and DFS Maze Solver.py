import time


class Node:
    # Each node represents a traveled square and contains a:
    #   - state: (y, x) index value it is currently representing
    #   - parent: previous node
    #   - action: action previous node took to get to current node (ie. up, down, left, right)
    def __init__(self, state, parent, action):
        # list [y, x] representing index positions in array
        self.state = state

        # type node
        # type None for parent node
        self.parent = parent

        # string 'U', 'D', 'L', 'R'
        # type None for parent node
        self.action = action


class StackFrontier:
    # Acts as main stack, holding each possible node that can be traveled to at a given moment
    def __init__(self):
        self.frontier = []

    # adds a node to the frontier
    def add(self, node):
        self.frontier.append(node)

    # checks if frontier is empty
    def is_empty(self):
        return len(self.frontier) == 0

    # returns and removes the last node in the stack
    def remove(self):
        if self.is_empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


# Acts as main queue, holding each possible node that can be traveled to at a given moment
class QueueFrontier(StackFrontier):
    # returns and removes the first node in the queue
    def remove(self):
        if self.is_empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


def find_start_end(maze):
    # Finds start point and end point in the maze
    start = [-1, -1]
    end = [-1, -1]

    for y in maze:
        for x in y:
            if x == 'S':
                start = [maze.index(y), y.index(x)]
            elif x == 'X':
                end = [maze.index(y), y.index(x)]

    return start, end


def display_solution(maze, solution):
    # remove all + symbols from if visualization was on
    for y in maze:
        for x in y:
            if x == '+':
                maze[maze.index(y)][y.index(x)] = ' '

    endpoints = find_start_end(maze)
    start = endpoints[0]

    for x in solution:
        if x == 'U':
            start[0] += 1
        elif x == 'D':
            start[0] -= 1
        elif x == 'R':
            start[1] += 1
        elif x == 'L':
            start[1] -= 1
        maze[start[0]][start[1]] = '+'

    maze[start[0]][start[1]] = 'S'
    maze[endpoints[1][0]][endpoints[1][1]] = 'X'

    for y in maze:
        print(y)


def solve(maze, start_point, end_point, frontier, visualize):
    # create frontier
    if frontier == 1:
        moves = StackFrontier()
    else:
        moves = QueueFrontier()

    start = Node([start_point[0], start_point[1]], None, None)
    moves.add(start)

    # check if start point was found
    if moves.is_empty():
        raise Exception("No startpoint")

    # create list to hold already visited nodes
    explored = list()

    # variable to keep track of how many different nodes have been explored
    iterations = 0

    while True:
        if moves.is_empty():
            raise Exception("No solution")

        # select a node from the frontier
        node = moves.remove()
        iterations += 1

        # check if node is end point
        if node.state == end_point:
            # list to hold all actions we took to reach this node
            actions = list()

            # begin backtracking until we reach the start point, keeping track of every action we took
            while node.parent is not None:
                actions.append(node.action)
                node = node.parent

            actions.reverse()
            print(f"Path length:         {len(actions)}")
            print(f"Total iterations:    {iterations}")
            return actions

        # add node to explored set so we don't revisit it again
        explored.append(node)

        # keep track of nodes y, x coordinates
        y = node.state[0]
        x = node.state[1]

        # expand node by moving up, down, right, left
        # only expanding if move exists and node has not already been visited
        if maze[y + 1][x] != '#' and not any(visited.state == [y + 1, x] for visited in explored):
            moves.add(Node([y + 1, x], node, 'U'))
        if maze[y - 1][x] != '#' and not any(visited.state == [y - 1, x] for visited in explored):
            moves.add(Node([y - 1, x], node, 'D'))
        if maze[y][x + 1] != '#' and not any(visited.state == [y, x + 1] for visited in explored):
            moves.add(Node([y, x + 1], node, 'R'))
        if maze[y][x - 1] != '#' and not any(visited.state == [y, x - 1] for visited in explored):
            moves.add(Node([y, x - 1], node, 'L'))

        if visualize:
            if maze[y][x] != 'S' and maze[y][x] != 'X':
                maze[y][x] = '+'
            for y in maze:
                print(y)
            time.sleep(1)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


maze = list()

maze.append(['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'])
maze.append(['#', ' ', ' ', ' ', ' ', 'S', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', 'X', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', '#', '#', ' ', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
maze.append(['#', ' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'])
maze.append(['#', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
maze.append(['#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
maze.append(['#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
maze.append(['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'])

endpoints = find_start_end(maze)

# second-last parameter = 1 for Depth-First Search and 0 for Breadth-First Search
# last parameter = true for maze visualization (see each step)
solution = solve(maze, endpoints[0], endpoints[1], 0, False)

display_solution(maze, solution)
