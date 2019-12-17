from processInputs import get_formatted_input
from intcode import IntcodeComputer

WIDTH = 41
HEIGHT = 59


def part1(data):
    def inf():
        return 0

    scanner = IntcodeComputer(data, inf)
    scanner.run_program()
    scaffold = [[]]
    for output in scanner.outputs:
        if output != 10:
            scaffold[-1].append(output)
        else:
            scaffold.append([])
    scaffold = scaffold[:-2]
    total = 0
    for y in range(len(scaffold) - 1):
        for x in range(len(scaffold[0]) - 1):
            if x == 0 or y == 0:
                continue
            if scaffold[y][x] in (35, 94):
                intersection = True
                for pair in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    if scaffold[y + pair[1]][x + pair[0]] == 46:
                        intersection = False
                if intersection:
                    total += x * y
    return total


# did this by hand lmao
COMMANDS = "65 44 66 44 65 44 66 44 67 44 66 44 67 44 65 44 67 44 67 10 82 44 49 50 44 76 44 49 48 44 76 44 49 48 10 76 44 54 44 76 44 49 50 44 82 44 49 50 44 76 44 52 10 76 44 49 50 44 82 44 49 50 44 76 44 54 10 110 10".split(
    " ")


def part2(data):
    data[0] = 2
    pointer = 0

    def inf():
        nonlocal pointer
        pointer += 1
        return COMMANDS[pointer - 1]

    robot = IntcodeComputer(data, inf)
    robot.outputs.append(0)
    robot.run_program()
    return robot.outputs[-1]


INPUT = get_formatted_input(17)
print(part1(INPUT), part2(INPUT))
