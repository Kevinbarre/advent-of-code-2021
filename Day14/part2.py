import sys
from collections import Counter
from pprint import pprint


def get_pairs(polymer):
    pairs = [polymer[i:i + 2] for i in range(0, len(polymer) - 1)]
    return Counter(pairs)


def step(polymer_pairs):
    new_polymer_pairs = {}
    for pair in polymer_pairs:
        insertion = rules[pair]
        left_pair = pair[0] + insertion
        right_pair = insertion + pair[1]

        if left_pair not in new_polymer_pairs:
            new_polymer_pairs[left_pair] = 0
        if right_pair not in new_polymer_pairs:
            new_polymer_pairs[right_pair] = 0

        new_polymer_pairs[left_pair] += polymer_pairs[pair]
        new_polymer_pairs[right_pair] += polymer_pairs[pair]

    return new_polymer_pairs


def count_letter_from_pairs(polymer_pairs, polymer):
    letters_count = {}
    # Count the letters from the pairs
    for pair in polymer_pairs:
        left = pair[0]
        right = pair[1]

        if left not in letters_count:
            letters_count[left] = 0
        if right not in letters_count:
            letters_count[right] = 0

        letters_count[left] += polymer_pairs[pair]
        letters_count[right] += polymer_pairs[pair]

    # Need to account that they are duplicated but the first and the last letter of the polymer
    # that appear each in only one pair. So we artificially add one to each, before dividing by 2
    letters_count[polymer[0]] += 1
    letters_count[polymer[-1]] += 1

    for letter in letters_count:
        letters_count[letter] //= 2

    return letters_count


template = input()
input()

rules = {}
for line in sys.stdin:
    left, right = line.rstrip('\n').split('->')
    rules[left.strip()] = right.strip()

template_pairs = get_pairs(template)
# print(template_pairs)

for s in range(1, 41):
    template_pairs = step(template_pairs)

# print(template_pairs)
counter = Counter(count_letter_from_pairs(template_pairs, template))
# print(counter)
most_common = counter.most_common()[0]
# print(most_common)
least_common = counter.most_common()[-1]
# print(least_common)

print("Result:", most_common[1] - least_common[1])
