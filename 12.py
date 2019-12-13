from copy import deepcopy

INPUT = [[16, -8, 13], [4, 10, 10], [17, -5, 6], [13, -3, 0]]
INITIAL_VELOCITY = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# INPUT = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]


def tick_simulation(positions, velocities):
    for m1 in range(len(positions)):
        for m2 in range(m1):
            m1_pos = positions[m1]
            m2_pos = positions[m2]
            for axis in range(3):
                if m1_pos[axis] > m2_pos[axis]:
                    velocities[m1][axis] -= 1
                    velocities[m2][axis] += 1
                elif m1_pos[axis] < m2_pos[axis]:
                    velocities[m1][axis] += 1
                    velocities[m2][axis] -= 1
    for m in range(len(positions)):
        pos = positions[m]
        vel = velocities[m]
        for axis in range(3):
            pos[axis] += vel[axis]
    return positions, velocities


def get_energy(positions, velocities):
    total_energy = 0
    for m in range(len(positions)):
        pos = positions[m]
        vel = velocities[m]
        pot = 0
        kin = 0
        for axis in range(3):
            pot += abs(pos[axis])
            kin += abs(vel[axis])
        total_energy += pot * kin
    return total_energy


def part1(data):
    positions = data
    velocities = deepcopy(INITIAL_VELOCITY)
    for time in range(1000):
        output = tick_simulation(positions, velocities)
        positions = output[0]
        velocities = output[1]
    return get_energy(positions, velocities)


def part2(data):
    axis_cycles = []
    for axis in range(3):
        positions = deepcopy(data)
        velocities = deepcopy(INITIAL_VELOCITY)
        initial_positions_axis = deepcopy([position[axis] for position in positions])
        initial_velocities_axis = deepcopy([velocity[axis] for velocity in velocities])
        positions_axis = initial_positions_axis
        velocities_axis = initial_velocities_axis
        cycle_time = 0
        while positions_axis != initial_positions_axis or velocities_axis != initial_velocities_axis or cycle_time == 0:
            output = tick_simulation(positions, velocities)
            positions = output[0]
            velocities = output[1]
            cycle_time += 1
            positions_axis = deepcopy([position[axis] for position in positions])
            velocities_axis = deepcopy([velocity[axis] for velocity in velocities])
        axis_cycles.append(cycle_time)
    return axis_cycles


print(part2(INPUT))
