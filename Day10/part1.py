import sys

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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
                return char
    return None


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

total = 0
for line in lines:
    corrupted_char = check_corrupted(line)
    if corrupted_char is not None:
        total += POINTS[corrupted_char]

print("Result:", total)
