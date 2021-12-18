import math
import sys
from enum import Enum, auto


class SnailfishNumber:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "SnailfishNumber(left=%r, right=%r)" % (self.left, self.right)

    def __str__(self):
        return "[{},{}]".format(self.left, self.right)

    def __add__(self, other):
        return SnailfishNumber(self, other)

    def left_depth(self):
        try:
            return self.left.depth()
        except AttributeError:
            return 0

    def right_depth(self):
        try:
            return self.right.depth()
        except AttributeError:
            return 0

    def depth(self):
        return max(self.left_depth(), self.right_depth()) + 1

    def magnitude(self):
        try:
            left_magnitude = self.left.magnitude()
        except AttributeError:
            left_magnitude = self.left

        try:
            right_magnitude = self.right.magnitude()
        except AttributeError:
            right_magnitude = self.right

        return 3 * left_magnitude + 2 * right_magnitude

    def add_to_left(self, value):
        try:
            self.left.add_to_left(value)
        except AttributeError:
            self.left += value

    def add_to_right(self, value):
        try:
            self.right.add_to_right(value)
        except AttributeError:
            self.right += value

    def add_to_left_of_right_child(self, value):
        try:
            # Add value to left of right child
            self.right.add_to_left(value)
        except AttributeError:
            # No right pair, just add to the right value
            self.right += value

    def add_to_right_of_left_child(self, value):
        try:
            # Add value to right of right child
            self.left.add_to_right(value)
        except AttributeError:
            # No right pair, just add to the left value
            self.left += value

    def reduce(self):
        while True:
            # First step is explode
            if self.depth() == 5:
                explode_snailfish(self)
                continue

            # Otherwise try to split
            split = self.split()
            if not split:
                # No split occured, the snailfish is fully reduce
                break

    def split(self):
        # Check if left element is higher than 9
        try:
            if self.left > 9:
                # Replace left with the new pair
                self.left = snailfish_from_split_value(self.left)
                # Confirm to parent that a split occured
                return True
        except TypeError:
            # Split left pair
            left_split = self.left.split()
            if left_split:
                # Confirm to parent that a split occured
                return True

        # Check if right element is higher than 9
        try:
            if self.right > 9:
                # Replace right with the new pair
                self.right = snailfish_from_split_value(self.right)
                # Confirm to parent that a split occured
                return True
        except TypeError:
            # Split right pair
            right_split = self.right.split()
            if right_split:
                # Confirm to parent that a split occured
                return True

        return False


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()


def parse_snailfish(string):
    if len(string) == 1:
        # Single number
        return int(string)
    else:
        # Identify comma separating both parts
        left_sublist_count = 0
        for i in range(1, len(string)):
            if string[i] == '[':
                left_sublist_count += 1
            elif string[i] == ']':
                left_sublist_count -= 1
            elif string[i] == ',' and left_sublist_count == 0:
                # Found the middle comma
                return SnailfishNumber(parse_snailfish(string[1:i]), parse_snailfish(string[i + 1:-1]))


def explode_snailfish(snailfish, depth=0):
    # print("In explode snailfish of {} with depth {}".format(snailfish, depth))
    # Time to explode
    if depth == 3:
        try:
            # Get left and right from left
            sub_left, sub_right = snailfish.left.left, snailfish.left.right
            # print("Sub_left {} and sub_right {} from left".format(sub_left, sub_right))
            # print("Add sub_right {} to left of right child {}".format(sub_right, snailfish.right))
            snailfish.add_to_left_of_right_child(sub_right)
            # Replace current left child by value 0
            snailfish.left = 0
            # print("Snailfish after adding to left : {}".format(snailfish))
            # sub_left must be returned to the parent to be added to the opposite pair
            return sub_left, Direction.LEFT
        except AttributeError:
            # Get left and right from right
            sub_left, sub_right = snailfish.right.left, snailfish.right.right
            # print("Sub_left {} and sub_right {} from right".format(sub_left, sub_right))
            # Left child has no pairs, or we wouldn't have ended in the except part
            # No left pair, just add sub_left to the left value
            # print("Add sub_left {} to the right of left child {}".format(sub_left, snailfish.left))
            snailfish.add_to_right_of_left_child(sub_left)
            # Replace current right child by value 0
            snailfish.right = 0
            # print("Snailfish after adding to right : {}".format(snailfish))
            # sub_right must be returned to the parent to be added to the opposite pair
            return sub_right, Direction.RIGHT

    else:
        # Otherwise check if exploding pair is on the left or right
        if snailfish.left_depth() >= snailfish.right_depth():
            # Explode on the left
            explosion_result = explode_snailfish(snailfish.left, depth + 1)
            # print("Explosion result from the left: {}".format(explosion_result))
            # Check if there are some more results of the explosion to propagate
            if explosion_result is not None:
                sub_value, direction = explosion_result
                if direction == Direction.RIGHT:
                    # print("Add {} to left of right child {}".format(sub_value, snailfish.right))
                    snailfish.add_to_left_of_right_child(sub_value)
                else:
                    # Propagate explosion to the parent
                    return sub_value, direction
        else:
            # Explode on the right
            explosion_result = explode_snailfish(snailfish.right, depth + 1)
            # print("Explosion result from the right: {}".format(explosion_result))
            # Check if there are some more results of the explosion to propagate
            if explosion_result is not None:
                sub_value, direction = explosion_result
                if direction == Direction.LEFT:
                    # print("Add {} to right of left child {}".format(sub_value, snailfish.right))
                    snailfish.add_to_right_of_left_child(sub_value)
                else:
                    # Propagate explosion to the parent
                    return sub_value, direction


def snailfish_from_split_value(value):
    half_value = value / 2
    # Left is rounded down
    left = math.floor(half_value)
    # Right is rounded up
    right = math.ceil(half_value)
    # Return new pair
    return SnailfishNumber(left, right)


numbers = []
for line in sys.stdin:
    numbers.append(parse_snailfish(line.rstrip('\n')))

result = None
for number in numbers:
    if not result:
        result = number
    else:
        result += number
    # print("Before reduce", result)
    result.reduce()
    # print("After reduce", result)

print("Final number: {}".format(result))
print("Magnitude: {}".format(result.magnitude()))
