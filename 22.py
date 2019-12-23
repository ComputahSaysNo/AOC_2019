from processInputs import get_formatted_input
from matplotlib import pyplot as plt


def part1(sequence, deck_size, pos):
    for line in sequence:
        if line == 'deal into new stack':
            pos = deck_size - pos - 1
            continue
        line = line.split(" ")
        if line[0] == "cut":
            amount = int(line[1])
            if amount >= 0:
                if pos < amount:
                    pos = (deck_size - amount) + pos
                else:
                    pos -= amount
            else:
                amount = abs(amount)
                if (deck_size - pos) <= amount:
                    pos = pos - (deck_size - amount)
                else:
                    pos += amount
        if line[0] == "deal":
            pos = (int(line[3]) * pos) % deck_size
    return pos


def calc_linear_map(sequence, deck_size):
    x = 1
    const = 0
    for line in sequence:
        if line == 'deal into new stack':
            x *= -1
            const *= -1
            const -= 1
            continue
        line = line.split(" ")
        if line[0] == 'cut':
            const -= int(line[1])
        if line[0] == 'deal':
            const *= int(line[3])
            x *= int(line[3])
    return x % deck_size, const % deck_size


def test(x):
    return (x * 29353735341940 + 81407565993874) % 119315717514047

def inv(x):
    return (29803531796010 * x + 73901765357410) % 119315717514047


INPUT = get_formatted_input(22)
print(test(2020))
print(part1(INPUT, 119315717514047, 2020))
print(inv(76041352231315))
print(inv(inv(2020)))