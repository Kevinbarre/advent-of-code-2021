import sys
from pprint import pprint


def get_nodes(i, j):
    nodes = {}
    # Left node
    if i - 1 > 0:
        nodes[(i - 1, j)] = WEIGHTS[j][i - 1]

    # Right node
    if i + 1 <= MAX_X:
        nodes[(i + 1, j)] = WEIGHTS[j][i + 1]

    # Bottom node
    if j + 1 <= MAX_Y:
        nodes[(i, j + 1)] = WEIGHTS[j + 1][i]

    # Top node
    if j - 1 > 0:
        nodes[(i, j - 1)] = WEIGHTS[j - 1][i]

    return nodes


WEIGHTS = []
for line in sys.stdin:
    WEIGHTS.append(list(map(int, line.rstrip('\n'))))

MAX_X = len(WEIGHTS[0]) - 1
MAX_Y = len(WEIGHTS) - 1

# print("MAX_X", MAX_X)
# print("MAX_Y", MAX_Y)

GRAPH = {(i, j): get_nodes(i, j) for i in range(MAX_X + 1) for j in range(MAX_Y + 1)}

# pprint(GRAPH)

# Dijkstra's algorithm adapted from https://stackoverflow.com/a/22899400
unvisited = {node: None for node in GRAPH}
visited = {}
current = (0, 0)
current_risk = 0
unvisited[current] = current_risk

while True:
    for neighbour, risk in GRAPH[current].items():
        if neighbour not in unvisited: continue
        new_risk = current_risk + risk
        if unvisited[neighbour] is None or unvisited[neighbour] > new_risk:
            unvisited[neighbour] = new_risk
    visited[current] = current_risk
    del unvisited[current]
    if not unvisited: break
    # print("Unvisited", unvisited)
    candidates = [node for node in unvisited.items() if node[1]]
    # print("Canditates", candidates)
    current, current_risk = sorted(candidates, key=lambda x: x[1])[0]

print("Result", visited[(MAX_X, MAX_Y)])
