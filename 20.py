DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse_input(filename):
    file = open(filename, 'rt')
    data = []
    maxWidth = 0
    for line in file:
        data.append(line.replace('\n', ''))
        if len(line) > maxWidth:
            maxWidth = len(line)
    data_copy = []
    for line in data:
        while len(line) < maxWidth:
            line += " "
        data_copy.append(line)
    return data_copy


def part_1_and_2(data):
    outputs = []
    height = len(data)
    width = len(data[0])
    portal_letters = {}
    for y in range(height):
        for x in range(width):
            char = data[y][x]
            if char.isalpha():
                for dx, dy in DELTAS:
                    if (x + dx) < 0 or (x + dx) >= width or (y + dy) < 0 or (y + dy) >= height:
                        continue
                    adj_char = data[y + dy][x + dx]
                    if adj_char in ('#', '.'):
                        code = data[y - dy][x - dx] + data[y][x]
                        if dy == - 1 or dx == -1:
                            code = code[::-1]
                        if code not in portal_letters:
                            portal_letters[code] = []
                        portal_letters[code].append((x + dx, y + dy))
    start = portal_letters['AA'][0]
    end = portal_letters['ZZ'][0]
    portals = {}
    for key in portal_letters:
        if len(portal_letters[key]) != 2:
            continue
        portals[portal_letters[key][0]] = portal_letters[key][1]
        portals[portal_letters[key][1]] = portal_letters[key][0]
    start = (start[0], start[1], 0)
    target = (end[0], end[1], 0)
    for part in (1, 2):
        node_queue = [start]
        visited = []
        prev = {}
        max_level = 100
        while len(node_queue) > 0:
            current = node_queue.pop(0)
            neighbours = []
            for dx, dy in DELTAS:
                if current[0] + dx < 0 or current[0] + dx >= width or current[1] + dy < 0 or current[1] + dy >= height:
                    continue
                if data[current[1] + dy][current[0] + dx] == '.':
                    neighbours.append((current[0] + dx, current[1] + dy, current[2]))
            if (current[0], current[1]) in portals:
                portal_exit = portals[(current[0], current[1])]
                if part == 1:
                    neighbours.append((portal_exit[0], portal_exit[1], 0))
                elif not (current[0] == 2 or current[0] == width - 4 or current[1] == 2 or current[1] == height - 3):
                    neighbours.append((portal_exit[0], portal_exit[1], current[2] + 1))
                elif current[2] != 0:
                    neighbours.append((portal_exit[0], portal_exit[1], current[2] - 1))
            for neighbour in neighbours:
                level = neighbour[2]
                if level > max_level:
                    continue
                if len(visited) <= level:
                    visited.append([[False] * width for i in range(height)])
                if not visited[level][neighbour[1]][neighbour[0]]:
                    visited[level][neighbour[1]][neighbour[0]] = True
                    node_queue.append(neighbour)
                    prev[neighbour] = current
        path = []
        at = target
        while at != start:
            path.append(at)
            at = prev[at]
        outputs.append(len(path))
    return outputs


INPUT = parse_input('inputs/20.txt')
print(part_1_and_2(INPUT))
