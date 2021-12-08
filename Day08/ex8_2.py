import sys


def decode_signal(signal):
    # Sort signal by length
    signal.sort(key=len)

    # First items are 1, 7 and 4
    one, seven, four = signal[:3]
    # print("One", one)
    # print("Seven", seven)
    # print("Four", four)

    # Signal Last item is 8
    eight = signal[-1]
    # print("Eight", eight)

    # Remaining elements to decode
    others_len5 = signal[3:6]  # 2 or 3 or 5
    others_len6 = signal[6:-1]  # 0, 6, 9
    # print("Others of length 5", others_len5)
    # print("Others of length 6", others_len6)

    # 3 is obtained using 1
    three = get_three(others_len5, one)
    others_len5.remove(three)
    # print("Three", three)
    # print("Others of length 5", others_len5)

    # 2 and 5 are obtained using 4
    two, five = get_two_five(others_len5, four)
    # print("Two", two)
    # print("Five", five)

    # 6 is obtained using 1
    six = get_six(others_len6, one)
    others_len6.remove(six)
    # print("Six", six)
    # print("Others of length 6", others_len5)

    # 9 and 0 are obtained using 4
    nine, zero = get_nine_zero(others_len6, four)
    # print("Nine", nine)
    # print("Zero", zero)

    return {
        sort_string(one): 1,
        sort_string(two): 2,
        sort_string(three): 3,
        sort_string(four): 4,
        sort_string(five): 5,
        sort_string(six): 6,
        sort_string(seven): 7,
        sort_string(eight): 8,
        sort_string(nine): 9,
        sort_string(zero): 0
    }


def get_three(len5, one):
    # 3 contains all segments of 1
    for digit in len5:
        if all(letter in digit for letter in one):
            return digit


def get_two_five(len5, four):
    first, second = len5
    # 2 has two digits in common with 4 whereas 5 has three digits in common with 4
    if len(set(first).intersection(four)) == 2:
        return first, second  # two, five
    else:
        return second, first  # five, two


def get_six(len6, one):
    # 6 does not contain all segments of 1, but 0 and 9 do
    for digit in len6:
        if not all(letter in digit for letter in one):
            return digit


def get_nine_zero(len6, four):
    # 9 contains all segments of 4, 0 does not
    first, second = len6
    if all(letter in first for letter in four):
        return first, second
    else:
        return second, first


def sort_string(string):
    return ''.join(sorted(string))


def decode_output(digits, output):
    # Sort output strings
    output = [sort_string(string) for string in output]
    # Compute 1000 * first digit + 100 * second digit + 10 * third digit + 1 * fourth digit
    return sum(digits[number] * 10 ** (3 - i) for i, number in enumerate(output))


lines = []
for line in sys.stdin:
    signal, output = line.rstrip('\n').split('|')
    lines.append((signal.split(), output.split()))

total = 0
for line in lines:
    line_signal, line_output = line
    digits = decode_signal(line_signal)
    # print(digits)
    line_output_value = decode_output(digits, line_output)
    total += line_output_value

print("Total:", total)
