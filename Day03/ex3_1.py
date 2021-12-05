import sys
from pprint import pprint

lines = []
for line in sys.stdin:
    lines.append(list(map(int, list(line.rstrip('\n')))))

# pprint(lines)

majority = int(len(lines) / 2)

total = [0] * len(lines[0])
for line in lines:
    for i, digit in enumerate(line):
        total[i] += digit

# print(majority)
# print(total)

gamma_rate = ''
for digit in total:
    if digit > majority:
        gamma_rate += '1'
    else:
        gamma_rate += '0'

print("Gamma rate binary: ", gamma_rate)

# Generate string of '1' of same length than gamma_rate
epsilon_rate = '1' * len(gamma_rate)

gamma_rate = int(gamma_rate, base=2)
epsilon_rate = int(epsilon_rate, base=2) - gamma_rate

result = gamma_rate * epsilon_rate

print("Gamma rate:", gamma_rate)
print("Epsilon rate:", epsilon_rate)
print("Result:", result)
