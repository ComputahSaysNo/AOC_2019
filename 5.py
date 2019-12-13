from intcode import IntcodeParser
from processInputs import get_formatted_input


def part1(data):
    def input_function():
        return 1

    computer = IntcodeParser(data, input_function)
    computer.run_program()
    return computer.outputs[-1]


def part2(data):
    def input_function():
        return 5

    computer = IntcodeParser(data, input_function)
    computer.run_program()
    return computer.outputs[-1]


INPUT = get_formatted_input(5)

print(part1(INPUT), part2(INPUT))
