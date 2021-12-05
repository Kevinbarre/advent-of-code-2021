import sys
from pprint import pprint


def draw_line(field, coordinates):
    # print(coordinates)
    a1, b1 = coordinates[0]
    a2, b2 = coordinates[1]

    if a1 == a2:
        # Draw vertical line
        # print("Vertical line")
        if b1 < b2:
            for j in range(b1, b2 + 1):
                field[j][a1] += 1
        else:
            for j in range(b2, b1 + 1):
                field[j][a1] += 1

    elif b1 == b2:
        # Draw horizontal line
        # print("Horizontal line")
        if a1 < a2:
            for i in range(a1, a2 + 1):
                field[b1][i] += 1
        else:
            for i in range(a2, a1 + 1):
                field[b1][i] += 1

    else:
        # Draw diagonal line
        # print("a1: {}, a2: {}, b1:{}, b2:{}".format(a1, a2, b1, b2))
        if a1 < a2:
            if b1 < b2:
                # print("Diagonal line from top left to bottom right")
                for i in range(a2 - a1 + 1):
                    field[b1 + i][a1 + i] += 1
            else:
                # print("Diagonal line from bottom left to top right")
                for i in range(a2 - a1 + 1):
                    field[b1 - i][a1 + i] += 1
        else:
            if b1 < b2:
                # print("Diagonal line from top right to bottom left")
                for i in range(a1 - a2 + 1):
                    field[b1 + i][a1 - i] += 1
            else:
                # print("Diagonal line from bottom right to top left")
                for i in range(a1 - a2 + 1):
                    field[b1 - i][a1 - i] += 1


lines = []
maximum = 0

for line in sys.stdin:
    first, second = line.rstrip('\n').split('->')
    x1, y1 = map(int, first.split(','))
    x2, y2 = map(int, second.split(','))

    maximum = max(maximum, x1, y1, x2, y2)
    lines.append([(x1, y1), (x2, y2)])

# pprint(lines)
# print("Maximum:", maximum)

grid = [[0] * (maximum + 1) for i in range(maximum + 1)]
# pprint(grid)

for line in lines:
    draw_line(grid, line)

# pprint(grid)

counter = sum(1 for row in grid for cell in row if cell > 1)
print(counter)
