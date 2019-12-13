from intcode import IntcodeParser
from processInputs import get_formatted_input
from itertools import permutations
from copy import deepcopy


def part1(data):
    amp_program = data
    inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    input_pointer = 0

    def input_function():
        nonlocal input_pointer
        output = inputs[input_pointer]
        input_pointer += 1
        return output

    phase_settings = permutations([0, 1, 2, 3, 4])
    outputs = []
    for phase_setting in phase_settings:
        input_pointer = 0
        inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(5):
            inputs[2 * j] = phase_setting[j]
        for amp in range(5):
            computer = IntcodeParser(deepcopy(amp_program), input_function)
            computer.run_program()
            if amp == 4:
                outputs.append(computer.outputs[0])
                break
            inputs[2 * amp + 3] = computer.outputs[0]
    return max(outputs)


def part2(data):
    amp_program = data
    phase_settings = permutations([5, 6, 7, 8, 9])
    max_output = 0
    for phase_setting in phase_settings:
        last_output = 0
        current_amp = 0
        phase_given = [False, False, False, False, False]

        def input_function():
            nonlocal last_output, phase_setting, current_amp, phase_given
            if not phase_given[current_amp]:
                output = phase_setting[current_amp]
                phase_given[current_amp] = True
            else:
                output = last_output
            return output

        computers = []
        for x in range(5):
            computers.append(IntcodeParser(deepcopy(amp_program), input_function))

        while not computers[4].stopped:
            last_output = computers[current_amp].get_next_output()
            current_amp = (current_amp + 1) % 5

        output = computers[4].outputs[-1]
        if output > max_output:
            max_output = output
    return max_output


INPUT = get_formatted_input(7)
print(part1(INPUT), part2(INPUT))
