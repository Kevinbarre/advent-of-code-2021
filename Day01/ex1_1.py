import sys

lines = []
for line in sys.stdin:
    lines.append(int(line.rstrip('\n')))

current = lines[0]
counter = 0

for line in lines[1:]:
    if line > current:
        counter += 1
    current = line

print(counter)
