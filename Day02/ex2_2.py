import sys

horizontal = 0
depth = 0
aim = 0

for line in sys.stdin:
    command, value = (line.rstrip('\n')).split()
    value = int(value)

    if command == 'forward':
        horizontal += value
        depth += aim * value
    elif command == 'down':
        aim += value
    else:  # command == 'up'
        aim -= value

result = horizontal * depth

print(result)
