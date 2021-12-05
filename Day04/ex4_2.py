import sys
from pprint import pprint


def mark_number(grid, number):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == number:
                grid[i][j] = None


def check_grid(grid):
    # Check rows
    for row in grid:
        if row == [None] * 5:
            return True

    # Check columns
    for row in list(map(list, zip(*grid))):
        if row == [None] * 5:
            return True

    return False


def play_game(grids, draws):
    current_grids = grids.copy()

    for draw in draws:
        if len(current_grids) == 1:
            grid = current_grids[0]
            # We have the loosing grid. Keep playing until it completes
            mark_number(grid, draw)
            if check_grid(grid):
                return draw, grid
        else:
            kept_grids = []
            for grid in current_grids:
                mark_number(grid, draw)
                if not check_grid(grid):
                    kept_grids.append(grid)
            current_grids = kept_grids


numbers = input().split(',')
print(numbers)

# Discard empty line after numbers
input()

bingos = []
current_bingo = []
for line in sys.stdin:
    if line == '\n':
        # Empty line marks end of bingo grid
        bingos.append(current_bingo)
        current_bingo = []
    else:
        current_bingo.append(line.split())
# Add last bingo grid
bingos.append(current_bingo)

pprint(bingos)

last_number, winning_grid = play_game(bingos, numbers)
print("Last number:", last_number)
print("Winning grid")
pprint(winning_grid)

total = sum(int(value) for row in winning_grid for value in row if value is not None)
print("Total:", total)

print("Result:", total * int(last_number))
