from processInputs import get_formatted_input
from intcode import IntcodeComputer


def part_1_and_2(data):
    outputs = []
    for part in (1, 2):
        packetQueue = []

        def inf():
            return -1

        network = [IntcodeComputer(data, inf) for i in range(50)]
        for i in range(50):
            network[i].give_next_input(i)
            packetQueue.append([])
        nat = [0, 0]
        history = []
        running = True
        while running:
            idle = True
            for i in range(len(network)):
                computer = network[i]
                queue = packetQueue[i]
                if len(queue) == 0:
                    computer.give_next_input(-1)
                else:
                    idle = False
                    while (len(queue)) > 0:
                        packet = queue.pop(0)
                        computer.give_next_input(packet[0])
                        computer.give_next_input(packet[1])
                while len(computer.outputs) > 0:
                    dest, x, y = computer.outputs[-3], computer.outputs[-2], computer.outputs[-1]
                    if dest == 255:
                        if part == 1:
                            outputs.append(y)
                            running = False
                        nat = [x, y]
                    else:
                        packetQueue[dest].append([x, y])
                    computer.outputs = computer.outputs[:-3]
            if idle:
                packetQueue[0].append(nat)
                history.append(nat)
                if len(history) > 2:
                    history.pop(0)
                    if history[-1][1] == history[-2][1]:
                        if history[-1][1] != 0:
                            outputs.append(history[-1][1])
                            return outputs


INPUT = get_formatted_input(23)
print(part_1_and_2(INPUT))
