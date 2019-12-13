from processInputs import get_formatted_input


def gen_tree(data):
    tree = {"COM": []}
    for line in data:
        line = line.split(')')
        parent = line[0]
        child = line[1]
        if parent not in tree:
            tree[parent] = []
        if child not in tree:
            tree[child] = []
        tree[parent].append(child)
    return tree


def part1(data):
    tree = gen_tree(data)
    current_depth = 0
    total_orbits = 0
    nodes_to_visit = ["COM"]
    while len(nodes_to_visit) != 0:
        total_orbits += current_depth * len(nodes_to_visit)
        next_layer = []
        for node in nodes_to_visit:
            next_layer = next_layer + tree[node]
        current_depth += 1
        nodes_to_visit = next_layer
    return total_orbits


def part2(data):
    tree = gen_tree(data)
    paths = []
    for target in ("YOU", "SAN"):
        path = []
        current = target
        while current != "COM":
            for node in tree:
                if current in tree[node]:
                    path.append(node)
                    current = node
                    break
        path.reverse()
        paths.append(path)
    common_length = 0
    for i in range(min([len(x) for x in paths])):
        if paths[0][i] == paths[1][i]:
            common_length += 1
        else:
            return sum([len(x[common_length:]) for x in paths])


INPUT = get_formatted_input(6)

print(part1(INPUT), part2(INPUT))
