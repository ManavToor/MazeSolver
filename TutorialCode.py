from queue import Queue
import time

maze = []

maze.append(['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'])
maze.append(['#', ' ', ' ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', 'X', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'])
maze.append(['#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
maze.append(['#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'])
maze.append(['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'])
maze.append(['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'])


def findStartAndEnd(maze):
    start = ()
    end = ()
  
    for y in maze:
        for x in y:
            if x == 'S':
                start = (maze.index(y), y.index(x))
            if x == 'X':
                end = (maze.index(y), y.index(x))
    return start, end


endpoints = findStartAndEnd(maze)


def printMaze(maze, sequence,):
    x = endpoints[0][1]
    y = endpoints[0][0]

    for i in sequence:
        if i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        elif i == 'D':
            y += 1
        elif i == 'U':
            y -= 1
        if maze[y][x] != 'X' and maze[y][x] != 'S':
            maze[y][x] = '+'

    for y in maze:
        print(y)
        #print('\033[F', end='')
    time.sleep(1)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


def findEnd(maze, moves_list):
    q = moves_list.get()
    try:
        moves = q
    except IndexError:
        moves = ""
   
    x = endpoints[0][1]
    y = endpoints[0][0]
  
    for m in moves:
        if m == 'L':
            x -= 1
        elif m == 'R':
            x += 1
        elif m == 'D':
            y += 1
        elif m == 'U':
            y -= 1
          
    printMaze(maze, moves)

    if x == endpoints[1][1] and y == endpoints[1][0]:
        quit()

    if maze[y][x-1] != '#':
        moves_list.put(q + 'L')
    if maze[y][x+1] != '#':
        moves_list.put(q + 'R')
    if maze[y-1][x] != '#':
        moves_list.put(q + 'U')
    if maze[y+1][x] != '#':
        moves_list.put(q + 'D')

    #print('\r' + str(x), end='')
    #time.sleep(1)


moves = Queue()
moves.put("")

while True:
  findEnd(maze, moves)
