import sys

lines = []
for line in sys.stdin:
    lines.append(int(line.rstrip('\n')))

current_window = sum(lines[0:3])
counter = 0

for i in range(3, len(lines)):
    new_window = current_window + lines[i] - lines[i - 3]
    if new_window > current_window:
        counter += 1
    current_window = new_window

print(counter)
