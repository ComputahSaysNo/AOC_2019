from processInputs import get_formatted_input
from math import atan2, pi


def part_1_and_2(data):
    asteroidPositions = []
    x = y = 0
    for line in data:
        x = 0
        for char in line:
            if char == '#':
                asteroidPositions.append((x, y))
            x += 1
        y += 1
    bestCount = 0
    bestPos = (0, 0)
    for pos1 in asteroidPositions:
        angles = set()
        for pos2 in asteroidPositions:
            if pos1 == pos2:
                continue
            angle = atan2(pos2[1] - pos1[1], pos2[0] - pos1[0])
            angles.add(angle)
        if len(angles) > bestCount:
            bestCount = len(angles)
            bestPos = pos1
    asteroidsByAngle = dict()
    laserPos = bestPos
    for pos in asteroidPositions:
        if pos == laserPos:
            continue
        angle = ((pi / 2) + atan2(pos[1] - laserPos[1], pos[0] - laserPos[0])) % (2 * pi)
        if angle not in asteroidsByAngle:
            asteroidsByAngle[angle] = []
        asteroidsByAngle[angle].append(pos)
    sortedAngles = sorted(asteroidsByAngle.keys())
    targetList = []

    def mag(elem):
        return elem[0] ** 2 + elem[1] ** 2

    for angle in sortedAngles:
        targetList.append(sorted(asteroidsByAngle[angle], key=mag, reverse=True))
    destroyed = 0
    pointer = 0
    currentDestroyed = (0, 0)
    while destroyed < 200:
        currentDestroyed = targetList[pointer].pop(0)
        destroyed += 1
        if not targetList[pointer]:
            targetList.remove([])
            pointer -= 1
        pointer = (pointer + 1) % len(targetList)
    return bestCount, 100 * currentDestroyed[0] + currentDestroyed[1]


INPUT = get_formatted_input(10)

print(part_1_and_2(INPUT))
