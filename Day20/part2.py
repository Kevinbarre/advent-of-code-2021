import sys
from copy import copy
from pprint import pprint


def step(image, s):
    # Extend image
    extended_image = extend_image(image, s)
    new_image = [['.'] * len(extended_image) for _ in range(len(extended_image))]

    for j in range(len(new_image)):
        for i in range(len(new_image)):
            new_image[j][i] = get_pixel(i, j, extended_image, s)

    return new_image


def extend_image(image, s):
    # Determine the default pixel to extend, depending on the step
    default_pixel = '.' if s % 2 == 0 else '#'
    extended_image = copy(image)
    # Add a dark lines at the top
    extended_image.insert(0, list(default_pixel * len(image)))
    # Add a dark lines at the bottom
    extended_image.append(list(default_pixel * len(image)))
    # Add a dark column on left and a dark column on right
    extended_image = [[default_pixel] + row + [default_pixel] for row in extended_image]
    # pprint(extended_image)
    return extended_image


def get_pixel(i, j, extended_image, s):
    pixels = ''.join(
        get_old_pixel_in_binary(k, l, extended_image, s) for k in range(j - 1, j + 2) for l in range(i - 1, i + 2))
    index = int(pixels, base=2)
    return ALGORITHM[index]


def get_old_pixel_in_binary(k, l, extended_image, s):
    length = len(extended_image)
    if k < 0 or k >= length or l < 0 or l >= length:
        # Determine the default pixel from infinity, depending on the step
        return '0' if s % 2 == 0 else '1'

    return '0' if extended_image[k][l] == '.' else '1'


def print_image(image):
    for row in image:
        print(''.join(row))


def count_lit_pixels(image):
    return sum(1 for row in image for pixel in row if pixel == '#')


ALGORITHM = input()
input()

input_image = []
for line in sys.stdin:
    input_image.append(list(line.rstrip('\n')))

# print("Base image")
# print_image(input_image)
STEPS = 50
for s in range(STEPS):
    input_image = step(input_image, s)
    # print("After step", s + 1)
    # print_image(input_image)

print("Result:", count_lit_pixels(input_image))
