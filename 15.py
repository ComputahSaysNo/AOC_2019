from processInputs import get_formatted_input
from intcode import IntcodeComputer
from copy import deepcopy


def part1(data):
    last_out = 1
    direction_pointer = 0
    DIRECTIONS = {1: (0, 1), 4: (1, 0), 2: (0, -1), 3: (-1, 0)}
    walls = set()
    current_pos = (0, 0)
    to_input = 1

    def turn_right():
        table = {1: 4, 2: 3, 3: 1, 4: 2}
        nonlocal to_input
        to_input = table[to_input]

    def turn_left():
        table = {1: 3, 2: 4, 3: 2, 4: 1}
        nonlocal to_input
        to_input = table[to_input]

    def inf():
        nonlocal to_input
        return to_input

    turtle = IntcodeComputer(data, inf)
    walls.add((current_pos[0], current_pos[1], 3))
    while True:
        turn_left()
        check_wall = turtle.get_next_output()
        while check_wall == 0:
            walls.add((current_pos[0] + DIRECTIONS[to_input][0], current_pos[1] + DIRECTIONS[to_input][1]))
            turn_right()
            check_wall = turtle.get_next_output()
        current_pos = (current_pos[0] + DIRECTIONS[to_input][0], current_pos[1] + DIRECTIONS[to_input][1])
        if check_wall == 2:
            walls.add((current_pos[0], current_pos[1], 2))
        if current_pos == (0, 0):
            break
    bounds = [0, 0, 0, 0]
    for wall in walls:
        if wall[0] < bounds[0]:
            bounds[0] = wall[0]
        if wall[0] > bounds[2]:
            bounds[2] = wall[0]
        if wall[1] < bounds[1]:
            bounds[1] = wall[1]
        if wall[1] > bounds[3]:
            bounds[3] = wall[1]
    maze = [[0 for j in range(bounds[2] - bounds[0] + 1)] for i in range(bounds[3] - bounds[1] + 1)]
    for wall in walls:
        if len(wall) == 3:
            maze[wall[1] - bounds[1]][wall[0] - bounds[0]] = wall[2]
        else:
            maze[wall[1] - bounds[1]][wall[0] - bounds[0]] = 1
    for line in maze:
        print("".join([str(x) for x in line]).replace("1", "█").replace("0", ' ').replace("2", "E"))
    return maze


def part2(data):
    maze = part1(data)
    age = 0
    prev_count = 0
    this_count = 1
    while prev_count != this_count:
        prev_count = this_count
        next_tick = deepcopy(maze)
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[x][y] == 2:
                    next_tick[x][y] = 2
                    for direction in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        try:
                            if next_tick[x + direction[0]][y + direction[1]] != 1:
                                next_tick[x + direction[0]][y + direction[1]] = 2
                        except IndexError:
                            pass
        age += 1
        this_count = 0
        for y in next_tick:
            for x in y:
                if x == 2:
                    this_count += 1
        maze = next_tick
    return age - 1


INPUT = get_formatted_input(15)
print(part2(INPUT))
