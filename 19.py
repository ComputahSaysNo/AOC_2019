from processInputs import get_formatted_input
from intcode import IntcodeComputer


def check(program, x, y):
    z = -1

    def inf():
        nonlocal x, y, z
        z += 1
        return [x, y][z]

    return IntcodeComputer(program, inf).get_next_output()


def part1(data):
    total = 0
    for y in range(50):
        for x in range(50):
            total += check(data, x, y)
    return total


def part2(data):
    bottom_edge = [9, 5]
    top_edge = [9, 4]
    square_found = False
    while not square_found:
        bottom_edge[0] += 1
        while check(data, bottom_edge[0], bottom_edge[1]) == 1:
            bottom_edge[1] += 1
        bottom_edge[1] -= 1
        top_edge[0] += 1
        while check(data, top_edge[0], top_edge[1]) != 1:
            top_edge[1] += 1
        if bottom_edge[1] - top_edge[1] >= 99:
            if check(data, bottom_edge[0] + 99, bottom_edge[1] - 99) == 1:
                square_found = True
    return bottom_edge[0] * 10000 + bottom_edge[1] - 99


INPUT = get_formatted_input(19)
print(part1(INPUT), part2(INPUT))
