from math import ceil


def parse_input_14(path):
    file = open(path, 'rt')
    reactions = dict()
    for line in file:
        line = line.rstrip().split(' => ')
        inputs = line[0].split(', ')
        output = line[1].split(' ')
        output = (output[1], int(output[0]))
        inputs = [(x[1], int(x[0])) for x in [x.split(' ') for x in inputs]]
        reactions[output[0]] = [inputs, output[1]]
    return reactions


def part1(data, num_to_make=1):
    stock = {}
    reactions = data
    ore_count = 0
    needed = [('FUEL', num_to_make)]
    while len(needed) > 0:
        line = needed[0]
        item = line[0]
        num_needed = line[1]
        if item == 'ORE':
            needed.remove(line)
            ore_count += num_needed
            continue
        if item in stock:
            if stock[item] > 0:
                if stock[item] <= num_needed:
                    num_needed -= stock[item]
                    stock[item] = 0
                else:
                    stock[item] -= num_needed
                    needed.remove(line)
                    continue
        way_to_make = reactions[item]
        batch_scale = ceil(num_needed / way_to_make[1])
        excess = batch_scale * way_to_make[1] - num_needed
        needed += [(pair[0], pair[1] * batch_scale) for pair in way_to_make[0]]
        if batch_scale * way_to_make[1] > num_needed:
            if item not in stock:
                stock[item] = 0
            stock[item] += excess
        needed.remove(line)
    return ore_count


def part2(data):
    target_ore = 1000000000000
    LB = 0
    UB = target_ore
    while UB - LB > 1:
        midpoint = (UB + LB) // 2
        ore_for_this_fuel = part1(data, midpoint)
        if ore_for_this_fuel < target_ore:
            LB = midpoint
        elif ore_for_this_fuel > target_ore:
            UB = midpoint
        else:
            return midpoint
    return LB


INPUT = parse_input_14('inputs/14.txt')
print(part1(INPUT), part2(INPUT))
