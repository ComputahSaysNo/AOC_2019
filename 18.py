from processInputs import get_formatted_input

INPUT = get_formatted_input(18)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Node:
    def __init__(self, name, pos, keys=None):
        if keys is None:
            keys = []
        self.name = name
        self.pos = pos
        self.children = []
        self.keys = keys
        if name != '@':
            self.keys.append(self.name)

    def add_child(self, name, pos):
        child = Node(name, pos, self.keys.copy())
        self.children.append(child)


def part1(data):
    start = (0, 0)
    width, height = len(data[0]), len(data)
    for y in range(height):
        for x in range(width):
            if data[y][x] == '@':
                start = (x, y)

    def check_reachable(s, keys):
        nq = [s]
        visited = [[False] * width for i in range(height)]
        prev = {}
        rkeys = []
        while len(nq) > 0:
            current = nq.pop(0)
            neighbours = []
            for dx, dy in DELTAS:
                if current[0] + dx < 0 or current[0] + dx >= width or current[1] + dy < 0 or current[1] + dy >= height:
                    continue
                val = data[current[1] + dy][current[0] + dx]
                if val == '.' or val.isupper() and val.lower() in keys or val.islower():
                    neighbours.append((current[0] + dx, current[1] + dy))
                if val.isalpha():
                    if val.islower():
                        if val not in keys:
                            rkeys.append((val, (current[0] + dx, current[1] + dy)))
            for neighbour in neighbours:
                if not visited[neighbour[1]][neighbour[0]]:
                    visited[neighbour[1]][neighbour[0]] = True
                    nq.append(neighbour)
                    prev[neighbour] = current
        return rkeys

    tree = Node('@', start)

    while True:
        node_queue = [tree]
        next_layer = []
        flag = False
        while not flag:
            next_layer = []
            flag = True
            for node in node_queue:
                if len(node.children) == 0:
                    next_layer.append(node)
                else:
                    next_layer += node.children
                    flag = False
            node_queue = next_layer.copy()

        for node in node_queue:
            reachable_keys = check_reachable(node.pos, node.keys)
            for key in reachable_keys:
                node.add_child(key[0], key[1])

        print("==============")
        try:
            print(len(tree.children))
            print(len(tree.children[0].children))
            print(len(tree.children[0].children[0].children))
            print(len(tree.children[0].children[0].children[0].children))
        except IndexError:
            pass





print(part1(INPUT))
