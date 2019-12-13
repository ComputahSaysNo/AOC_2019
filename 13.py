from processInputs import get_formatted_input
from intcode import IntcodeParser


def part1(data):
    def inf():
        return 0

    computer = IntcodeParser(data, inf)
    computer.run_program()
    programOutput = computer.outputs
    i = 0
    blocks = set()
    while i < len(programOutput):
        if programOutput[i + 2] == 2:
            blocks.add((programOutput[i], programOutput[i + 1]))
        if programOutput[i + 2] != 2:
            try:
                blocks.remove((programOutput[i], programOutput[i + 1]))
            except KeyError:
                pass
        i += 3
    return len(blocks)


def part2(data):
    data[0] = 2
    ballX = 0
    paddleX = 0

    def inf():
        nonlocal paddleX, ballX
        if paddleX > ballX:
            return -1
        if paddleX < ballX:
            return 1
        return 0

    computer = IntcodeParser(data, inf)
    while not computer.stopped:
        tileData = []
        for i in range(3):
            tileData.append(computer.get_next_output())
        if tileData[2] == 3:
            paddleX = tileData[0]
        if tileData[2] == 4:
            ballX = tileData[0]
    return computer.outputs[-1]


INPUT = get_formatted_input(13)
print(part1(INPUT), part2(INPUT))
