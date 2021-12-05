import sys

movements = {'forward': 0, 'down': 0, 'up': 0}
for line in sys.stdin:
    command, value = (line.rstrip('\n')).split()
    movements[command] += int(value)

# print(movements)

result = movements['forward'] * (movements['down'] - movements['up'])

print(result)
