import sys


def is_low_point(current, left, right, top, bottom):
    return current < left and current < right and current < top and current < bottom


def should_explore(value, point, basin, explorable_points):
    return value != 9 and point not in basin and point not in explorable_points


def search_basin(low_point, locations):
    # print("Low point:", low_point)
    basin = set()
    explorable_points = {low_point}

    while explorable_points:
        # print("Explorable_points", explorable_points)
        # Get next explorable point
        explorable_point = explorable_points.pop()
        # Add it to the basin
        basin.add(explorable_point)
        # Check neighbours
        i, j = explorable_point
        # Left
        if j - 1 >= 0:
            left = locations[i][j - 1]
            left_point = (i, j - 1)
            if should_explore(left, left_point, basin, explorable_points):
                explorable_points.add(left_point)
        # Right
        try:
            right = locations[i][j + 1]
            right_point = (i, j + 1)
            if should_explore(right, right_point, basin, explorable_points):
                explorable_points.add(right_point)
        except IndexError:
            pass
        # Top
        if i - 1 >= 0:
            top = locations[i - 1][j]
            top_point = (i - 1, j)
            if should_explore(top, top_point, basin, explorable_points):
                explorable_points.add(top_point)
        # Bottom
        try:
            bottom = locations[i + 1][j]
            bottom_point = (i + 1, j)
            if should_explore(bottom, bottom_point, basin, explorable_points):
                explorable_points.add(bottom_point)
        except IndexError:
            pass

    # print("Basin", basin)
    return basin


lines = []
for line in sys.stdin:
    lines.append(list(map(int, line.rstrip('\n'))))

low_points = []
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
            low_points.append((i, j))

print("Low points:", low_points)

basins = []
for low_point in low_points:
    # Get corresponding basin of the low_point
    basins.append(search_basin(low_point, lines))

print("Basins:", basins)

# Get 3 biggest basins
basins.sort(key=len, reverse=True)
first, second, third = basins[:3]
result = len(first) * len(second) * len(third)

print("Result", result)
