import sys

first = sys.stdin.readline().strip().split(" ")

while (first):
    # if length, width = 0, stop
    if (int(first[0]) == 0 and int(first[1]) == 0):
        break

    width = int(first[0])
    length = int(first[1])
    # number of steps
    second = int(sys.stdin.readline().strip())

    actual_x = 0
    actual_y = 0

    robot_x = 0
    robot_y = 0

    #for each move
    for index in range(second):
        line = sys.stdin.readline().strip().split(" ")
        dir = line[0]
        move = int(line[1])

        if dir == 'u':
            # if going up, the maximum position cannot be above length - 1
            actual_y = min(length - 1, actual_y + move)
            robot_y += move 
        if dir == 'd':
            # if going down, the minimum position cannot be below 0
            actual_y = max(0, actual_y - move)
            robot_y -= move 
        if dir == 'r':
            # if going right, the maximum position cannot be above width - 1
            actual_x = min(width - 1, actual_x + move)
            robot_x += move 
        if dir == 'l':
            # if going left, the maximum position cannot be below 0
            actual_x = max(0, actual_x - move)
            robot_x -= move 
    print("Robot thinks " + str(robot_x) + " " + str(robot_y))
    print("Actually at " + str(actual_x) + " " + str(actual_y))
    print()

    first = sys.stdin.readline().strip().split(" ")


