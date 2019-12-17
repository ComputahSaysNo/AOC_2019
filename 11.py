from processInputs import get_formatted_input
from intcode import IntcodeComputer

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def run_turtle(initial, program):
    white_tiles = initial
    painted_tiles = set()
    current_pos = (0, 0)
    directionPointer = 0

    def input_function():
        return 1 if (current_pos in white_tiles) else 0

    turtle = IntcodeComputer(program, input_function)
    while not turtle.stopped:
        painted_tiles.add(current_pos)
        colour = turtle.get_next_output()
        if colour == 0:
            try:
                white_tiles.remove(current_pos)
            except KeyError:
                pass
        if colour == 1:
            white_tiles.add(current_pos)
        turn = turtle.get_next_output()
        if turn == 0:
            directionPointer = (directionPointer - 1) % 4
        if turn == 1:
            directionPointer = (directionPointer + 1) % 4
        direction = DIRECTIONS[directionPointer]
        current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    return white_tiles, painted_tiles


def part1(data):
    initial = set()
    result = run_turtle(initial, data)[1]
    return len(result)


def part2(data):
    initial = {(0, 0)}
    image = "\n"
    result = run_turtle(initial, data)
    for y in range(10, -10, -1):
        row = ""
        for x in range(50):
            if (x, y) in result[0]:
                row += "███"
            else:
                row += "   "
        image += row + "\n"
    return image


INPUT = get_formatted_input(11)
print(part2(INPUT))
