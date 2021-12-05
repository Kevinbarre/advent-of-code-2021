import sys
from pprint import pprint

lines = []
for line in sys.stdin:
    lines.append(list(map(int, list(line.rstrip('\n')))))

oxygen_lines = lines.copy()
print("=== Oxygen ===")
pprint(oxygen_lines)

bit = 0
while len(oxygen_lines) > 1:
    print("--- Bit {} ---".format(bit))
    majority = len(oxygen_lines) / 2
    count = sum(oxygen_line[bit] for oxygen_line in oxygen_lines)

    print("Majority: ", majority)
    print("Count: ", count)

    # Majority of 1 ( including same amount)
    if count >= majority:
        # Keep values with a 1 at position bit
        winning_bit = 1
    else:
        # Keep values with a 0 at position bit
        winning_bit = 0
    print("Winning bit is: ", winning_bit)
    oxygen_lines = [oxygen_line for oxygen_line in oxygen_lines if oxygen_line[bit] == winning_bit]
    pprint(oxygen_lines)
    bit += 1

oxygen = int(''.join((str(digit) for digit in oxygen_lines[0])), base=2)
print("Oxygen: ", oxygen)

co2_lines = lines.copy()
print("=== CO2 ===")
pprint(co2_lines)

bit = 0
while len(co2_lines) > 1:
    print("--- Bit {} ---".format(bit))
    majority = len(co2_lines) / 2
    count = sum(co2_line[bit] for co2_line in co2_lines)

    print("Majority: ", majority)
    print("Count: ", count)

    # Majority of 1 ( including same amount)
    if count >= majority:
        # Keep values with a 0 at position bit
        winning_bit = 0
    else:
        # Keep values with a 1 at position bit
        winning_bit = 1
    print("Winning bit is: ", winning_bit)
    co2_lines = [co2_line for co2_line in co2_lines if co2_line[bit] == winning_bit]
    pprint(co2_lines)
    bit += 1

co2 = int(''.join((str(digit) for digit in co2_lines[0])), base=2)
print("CO2: ", co2)

result = oxygen * co2
print("Result:", result)
