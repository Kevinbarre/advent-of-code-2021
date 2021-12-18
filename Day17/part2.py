def step(x_position, y_position, x_velocity, y_velocity):
    x_position += x_velocity
    y_position += y_velocity
    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1
    y_velocity -= 1

    return x_position, y_position, x_velocity, y_velocity


def perform_simulation(x_velocity, y_velocity, x_target, y_target):
    x, y = 0, 0

    while can_still_reach_target(x, y, x_velocity, y_velocity, x_target, y_target):
        x, y, x_velocity, y_velocity = step(x, y, x_velocity, y_velocity)
        if is_in_target(x, y, x_target, y_target):
            return True
    return False


def can_still_reach_target(x_position, y_position, x_velocity, y_velocity, x_target, y_target):
    can_reach_x = (x_position < x_target[0] and x_velocity > 0) or (x_position > x_target[1] and x_velocity < 0) or (
            x_target[0] <= x_position <= x_target[1])
    can_reach_y = y_position > y_target[0] or (y_position < y_target[1] and y_velocity > 0) or (
            y_target[0] <= y_position <= y_target[1])

    return can_reach_x and can_reach_y


def is_in_target(x_position, y_position, x_target, y_target):
    return x_target[0] <= x_position <= x_target[1] and y_target[0] <= y_position <= y_target[1]


def find_all_velocity(x_target, y_target):
    count = 0
    for x_velocity in range(x_target[1] + 1):
        for y_velocity in range(-abs(y_target[0]), abs(y_target[0])):
            simulation_result = perform_simulation(x_velocity, y_velocity, x_target, y_target)
            if simulation_result:
                # print("{}, {}".format(x_velocity, y_velocity))
                count += 1

    return count


_, coordinates = input().split(':')

x_part, y_part = coordinates.split(',')

min_x, max_x = map(int, x_part.split('=')[1].split('..'))
min_y, max_y = map(int, y_part.split('=')[1].split('..'))

# print("Min x: {}, Max x: {}".format(min_x, max_x))
# print("Min y: {}, Max y: {}".format(min_y, max_y))

result = find_all_velocity((min_x, max_x), (min_y, max_y))

print("Result:", result)
