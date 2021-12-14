import sys
from collections import Counter
from pprint import pprint


def step(polymer):
    new_chain = ''
    for i in range(0, len(polymer) - 1):
        pair = polymer[i:i + 2]
        # Only add left part + the inserted one. Right part will be inserted as left part of next i
        new_chain += pair[0] + rules[pair]
    # Add last element of the polymer to complete the chain
    return new_chain + polymer[-1]


template = input()
input()

rules = {}
for line in sys.stdin:
    left, right = line.rstrip('\n').split('->')
    rules[left.strip()] = right.strip()

print("Template:", template)
# print(rules)


for s in range(1, 11):
    template = step(template)
    print("After step {}: {}".format(s, template))

counter = Counter(template)
most_common = counter.most_common()[0]
# print(most_common)
least_common = counter.most_common()[-1]
# print(least_common)

print("Result:", most_common[1] - least_common[1])
