from processInputs import get_formatted_input


def part1(data):
    total = 0
    for mass in data:
        total += (mass // 3) - 2
    return total


def part2(data):
    total = 0
    for mass in data:
        fuel_bits = [(mass // 3) - 2]
        while fuel_bits[-1] > 6:
            fuel_bits.append((fuel_bits[-1] // 3) - 2)
        total += sum(fuel_bits)
    return total


INPUT = get_formatted_input(1)

print(part1(INPUT), part2(INPUT))
