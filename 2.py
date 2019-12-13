from processInputs import get_formatted_input
from copy import deepcopy

ADD = 1
MULT = 2
STOP = 99


def part1(data, noun=12, verb=2):
    data[1] = noun
    data[2] = verb
    pointer = 0
    running = True
    while running:
        next_instruction = pointer + 4
        if data[pointer] == ADD:
            data[data[pointer + 3]] = data[data[pointer + 1]] + data[data[pointer + 2]]
        elif data[pointer] == MULT:
            data[data[pointer + 3]] = data[data[pointer + 1]] * data[data[pointer + 2]]
        elif data[pointer] == STOP:
            running = False
        pointer = next_instruction
    return data[0]


def part2(data):
    for x in range(100):
        for y in range(100):
            initial = deepcopy(data)
            output = part1(initial, x, y)
            if output == 19690720:
                return 100 * x + y


INPUT = get_formatted_input(2)

print(part1(INPUT), part2(INPUT))
