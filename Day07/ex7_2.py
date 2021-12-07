from collections import Counter


def compute_fuel(crabs, target_position):
    total_fuel = 0
    for crab, count in crabs.items():
        steps = abs(crab - target_position)
        total_fuel += steps * (steps + 1) * count // 2
    return total_fuel


initial_positions = Counter(map(int, input().split(',')))

# print("Initial positions", initial_positions)

maximum = max(initial_positions)

# print("Maximum", maximum)

less_fuel = float('inf')
for i in range(0, maximum + 1):
    less_fuel = min(less_fuel, compute_fuel(initial_positions, i))

print("Result", less_fuel)
