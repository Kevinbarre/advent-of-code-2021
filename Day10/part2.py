import sys

POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

DELIMITERS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def check_corrupted(string):
    expected_closing_chars = []
    for char in string:
        if char in DELIMITERS:
            # Opening char found, add corresponding closing char to the expected ones
            expected_closing_chars.append(DELIMITERS[char])
        else:
            # Closing char found, check that the next expected one is matching
            next_expected = expected_closing_chars.pop()
            if next_expected != char:
                return False
    expected_closing_chars.reverse()
    return ''.join(expected_closing_chars)


def get_score(string):
    score = 0
    for char in string:
        score *= 5
        score += POINTS[char]
    return score


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

closing_lines = []
for line in lines:
    expected_closing_chars = check_corrupted(line)
    if expected_closing_chars:
        closing_lines.append(expected_closing_chars)

# print("Closing lines", closing_lines)

scores = []
for closing_line in closing_lines:
    closing_line_score = get_score(closing_line)
    # print("{} - {} total points.".format(closing_line, closing_line_score))
    scores.append(closing_line_score)

scores.sort()
# Get middle score
result = scores[len(scores) // 2]

print("Result:", result)
