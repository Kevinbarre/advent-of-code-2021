from collections import Counter


def compute_fuel(crabs, target_position):
    total_fuel = 0
    for crab, count in crabs.items():
        total_fuel += abs(crab - target_position) * count
    return total_fuel


initial_positions = Counter(map(int, input().split(',')))

# print("Initial positions", initial_positions)

maximum = max(initial_positions)

# print("Maximum", maximum)

less_fuel = float('inf')
for i in range(0, maximum + 1):
    less_fuel = min(less_fuel, compute_fuel(initial_positions, i))

print("Result", less_fuel)
