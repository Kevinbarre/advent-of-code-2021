import sys
from pprint import pprint


def fold(paper, instruction):
    direction, value = instruction

    if direction == 'y':
        return fold_up(paper, value)
    else:
        return fold_left(paper, value)


def fold_up(paper, value):
    for y in range(value + 1, len(paper)):
        for x in range(len(paper[y])):
            if paper[y][x] == '#':
                # Report dot on the upper part of the paper
                paper[2 * value - y][x] = '#'
    return paper[:value]


def fold_left(paper, value):
    for x in range(value + 1, len(paper[0])):
        for y in range(len(paper)):
            if paper[y][x] == '#':
                # Report dot on the left part of the paper
                paper[y][2 * value - x] = '#'
    return [row[:value] for row in paper]


def count_dots(paper):
    return sum(1 for row in paper for cell in row if cell == '#')


dots = []
max_x = 0
max_y = 0
for line in sys.stdin:
    if line == '\n':
        break
    line_x, line_y = map(int, line.rstrip('\n').split(','))
    max_x = max(line_x, max_x)
    max_y = max(line_y, max_y)
    dots.append((line_x, line_y))

instructions = []
for line in sys.stdin:
    last_part = line.rstrip('\n').split()[-1]
    dir, val = last_part.split('=')
    instructions.append((dir, int(val)))

# print(dots)
# print(max_x)
# print(max_y)
# print(instructions)


transparent_paper = [['.'] * (max_x + 1) for _ in range(max_y + 1)]
# pprint(transparent_paper)

for dot in dots:
    dot_x, dot_y = dot
    transparent_paper[dot_y][dot_x] = '#'
# pprint(transparent_paper)

transparent_paper = fold(transparent_paper, instructions[0])
# pprint(transparent_paper)

print("Result", count_dots(transparent_paper))
