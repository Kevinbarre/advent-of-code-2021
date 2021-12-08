import sys

lines = []
for line in sys.stdin:
    signal, output = line.rstrip('\n').split('|')
    lines.append((signal.split(), output.split()))

total = 0
for line in lines:
    output = line[1]
    total += sum(1 for digit in output if len(digit) in (2, 3, 4, 7))

print("Total:", total)
