import sys
from pprint import pprint


def flash(k, l, state, flashings):
    state[k][l] += 1
    if state[k][l] == 10:
        flashings.append((k, l))


def step(state):
    # First increment everything by 1, and check if it's flashing
    flashings = []
    for i in range(10):
        for j in range(10):
            state[i][j] += 1
            if state[i][j] == 10:
                flashings.append((i, j))

    # Flashing octopus propagate to their neighbours
    while flashings:
        i, j = flashings.pop()
        # Increment flashing neighbours by 1
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if k == i and l == j:
                    # Ignore current cell
                    continue
                if 0 <= k < 10 and 0 <= l < 10:  # Only flash valid cells
                    flash(k, l, state, flashings)

    # Count number of flashs, and reset them to 0
    nb_flash = 0
    for i in range(10):
        for j in range(10):
            if state[i][j] >= 10:
                state[i][j] = 0
                nb_flash += 1

    return nb_flash == 100


octopuses = []
for line in sys.stdin:
    octopuses.append(list(map(int, line.rstrip('\n'))))

print("Before any steps:")
pprint(octopuses)

s = 1
while True:
    all_flashing = step(octopuses)
    print("After step {}:".format(s))
    pprint(octopuses)
    if all_flashing:
        print("All flashing at step:", s)
        break
    s += 1
