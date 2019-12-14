from processInputs import get_formatted_input

DIRECTIONS = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


def part1_and_2(data):
    wire_points = []
    for i in range(len(data)):
        wire_points.append([])
        current_pos = (0, 0)
        for segment in data[i]:
            direction = DIRECTIONS[segment[0]]
            for j in range(int(segment[1:])):
                wire_points[i].append(current_pos)
                current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    intersections = set(wire_points[0]) & set(wire_points[1])
    intersections.remove((0, 0))
    return (min([abs(x) + abs(y) for (x, y) in intersections]),
            min(sum(wire.index(intersect) for wire in wire_points) for intersect in intersections))


INPUT = get_formatted_input(3)
print(part1_and_2(INPUT))
