import sys


def is_low_point(current, left, right, top, bottom):
    return current < left and current < right and current < top and current < bottom


lines = []
for line in sys.stdin:
    lines.append(list(map(int, line.rstrip('\n'))))

total = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        current = lines[i][j]
        if j - 1 >= 0:
            left = lines[i][j - 1]
        else:
            left = 10
        try:
            right = lines[i][j + 1]
        except IndexError:
            right = 10
        if i - 1 >= 0:
            top = lines[i - 1][j]
        else:
            top = 10
        try:
            bottom = lines[i + 1][j]
        except IndexError:
            bottom = 10
        if is_low_point(current, left, right, top, bottom):
            total += (1 + current)
            # print("i: {}, j: {}, current: {}".format(i, j, current))

print("Result:", total)
