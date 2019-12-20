from processInputs import get_formatted_input

INPUT = get_formatted_input(18)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def part1(data):
    doors = ALPHABET.upper()
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    keys = ALPHABET.lower()
    maze = []
    currentX = currentY = 0
    for y in range(len(data)):
        maze.append([])
        for x in range(len(data[0])):
            if data[y][x] == '@':
                currentX = x
                currentY = y
                maze[y].append('.')
            else:
                maze[y].append(data[y][x])
    end_search = False
    currently_reachable = set()
    while not end_search:
        for pos in currently_reachable:
            for direction in DIRECTIONS:
                test_pos = maze[pos[0] + direction[0]][pos[1]]



print(part1(INPUT))
