from intcode import IntcodeParser
from processInputs import get_formatted_input


def part1_and_2(data):
    outputs = []
    for i in (1, 2):
        def inf():
            return i

        computer = IntcodeParser(data, inf)
        computer.run_program()
        outputs.append(computer.outputs[0])
    return outputs


INPUT = get_formatted_input(9)
print(part1_and_2(INPUT))
