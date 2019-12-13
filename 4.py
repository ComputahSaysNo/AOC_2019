INPUT = '231832-767346'


def part1_and_2(data):
    bounds = [int(x) for x in data.split('-')]
    num_valid = [0, 0]
    for i in range(bounds[0], bounds[1]):
        i = str(i)
        not_descending = True
        double = False
        double_but_not_group = False
        for j in range(len(i) - 1):
            if i[j + 1] < i[j]:
                not_descending = False
            if i[j] == i[j + 1]:
                double = True
                if j == 0 or i[j - 1] != i[j]:
                    if j >= len(i) - 2 or i[j + 2] != i[j]:
                        double_but_not_group = True
        if not_descending:
            if double:
                num_valid[0] += 1
                if double_but_not_group:
                    num_valid[1] += 1

    return num_valid


print(part1_and_2(INPUT))
