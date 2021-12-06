def new_day(fishes):
    new_fishes = []
    for fish in fishes:
        if fish == 0:
            # New fish is born
            new_fishes.append(6)
            new_fishes.append(8)
        else:
            new_fishes.append(fish - 1)
    return new_fishes


lantern_fishes = list(map(int, input().split(',')))

# print("Initial state:", lantern_fishes)

for i in range(0, 80):
    lantern_fishes = new_day(lantern_fishes)
    # print("After {} day: {}".format(i+1, lantern_fishes))

print("Result:", len(lantern_fishes))
