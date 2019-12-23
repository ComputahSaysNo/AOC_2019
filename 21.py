from processInputs import get_formatted_input
from intcode import IntcodeComputer


def part_1_and_2(data):
    outputs = []
    scripts = ["NOT A T \n NOT T T \n AND B T \n AND C T \n NOT T T \n AND D T \n NOT T J \n NOT J J \n WALK \n",
               "NOT C J \n AND H J \n NOT B T \n OR T J \n NOT A T \n OR T J \n AND D J \n RUN \n"]
    for i in range(2):
        pointer = 0

        def inf():
            nonlocal scripts, pointer
            pointer += 1
            return ord(scripts[i][pointer - 1])

        computer = IntcodeComputer(data, inf)
        computer.run_program()
        outputs.append(computer.outputs[-1])
    return outputs


INPUT = get_formatted_input(21)
print(part_1_and_2(INPUT))
