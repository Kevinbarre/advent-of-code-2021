from collections import Counter


def new_day(fishes):
    new_fishes = {}
    for days in fishes:
        if days not in (0, 7):
            new_fishes[days - 1] = fishes[days]

    # Specific operation for new born
    new_fishes[8] = fishes.get(0, 0)

    # Fishes of value 6 are those giving birth at 0 + the existing ones from 7
    new_fishes[6] = fishes.get(0, 0) + fishes.get(7, 0)

    return new_fishes


lantern_fishes = Counter(map(int, input().split(',')))

print("Initial state:", lantern_fishes)

for i in range(0, 256):
    lantern_fishes = new_day(lantern_fishes)
    print("After {} day: {}".format(i + 1, lantern_fishes))

print("Result:", sum(value for value in lantern_fishes.values()))
