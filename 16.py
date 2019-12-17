from processInputs import get_formatted_input

BASE_PATTERN = [0, 1, 0, -1]


def run_ftt(sample, phases):
    sample = str(sample)
    signal_length = len(sample)
    for i in range(phases):
        output = []
        for j in range(signal_length):
            this_total = 0
            for k in range(signal_length):
                this_total = this_total + BASE_PATTERN[((k + 1) % (4 * (j + 1)) // (j + 1))] * int(sample[k])
            output.append(str(abs(this_total) % 10))
        sample = "".join(output)

    return sample


def part1(data):
    return run_ftt(data, 100)[:8]


def part2(data):
    data = data * 10000
    signal = data[int(data[:7]):]
    print(len(signal))
    phases = 100
    for i in range(phases):
        output = []
        this_total = sum([int(signal[x]) for x in range(len(signal))])
        for k in range(len(signal)):
            output.append(this_total % 10)
            this_total -= int(signal[k])
        signal = "".join(str(x) for x in output)
    return signal[:8]


INPUT = str(get_formatted_input(16))
print(part1(INPUT), part2(INPUT))
