import sys
from pprint import pprint


def get_all_paths():
    all_paths = []
    current_paths = [(['start'], None)]  # None will store the first small cave already visited
    while current_paths:
        current_path = current_paths.pop()
        new_paths_with_visited_cave = get_paths(current_path)
        for new_path_with_visited_cave in new_paths_with_visited_cave:
            new_path, _ = new_path_with_visited_cave
            if new_path[-1] == 'end':
                # Exit found, we save this path as a result
                all_paths.append(new_path)
            else:
                # Not an exit yet, we'll search from here
                current_paths.append(new_path_with_visited_cave)

    return all_paths


def get_paths(current_path_with_visited_cave):
    current_path, visited_cave = current_path_with_visited_cave
    # print("Current path", current_path)
    # print("Visited cave", visited_cave)
    current_cave = current_path[-1]
    possible_exits = CAVES[current_cave]
    possibles_paths = []
    for possible_exit in possible_exits:
        new_visited_cave = visited_cave
        # print("Possible exit", possible_exit)
        # Ignore small caves we've already visited, except the first one
        if possible_exit.islower() and possible_exit in current_path:
            if visited_cave:  # Already visited a cave twice, we cannot visit another one twice
                # print("Skip this")
                continue
            else:
                new_visited_cave = possible_exit
                # print("New visited cave", new_visited_cave)
        new_path = current_path.copy()
        new_path.append(possible_exit)
        possibles_paths.append((new_path, new_visited_cave))
    # print("Possible paths:", possibles_paths)
    return possibles_paths


CAVES = {}
for line in sys.stdin:
    first, second = line.rstrip('\n').split('-')
    if first not in CAVES:
        CAVES[first] = []
    if second not in CAVES:
        CAVES[second] = []

    if second != 'start':
        CAVES[first].append(second)

    if first != 'start':
        CAVES[second].append(first)

# print("Caves")
# pprint(CAVES)

all_paths = get_all_paths()
# print("Paths found")
# pprint(all_paths)

print("Result", len(all_paths))
