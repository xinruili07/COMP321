#list where the left-most element represent the ball
cups = [True, False, False]
#receives the string of inputs
string_of_moves = input()

#iterate through each input
for index in range(len(string_of_moves)):

    #input A swaps cup 1 with cup 2
    if string_of_moves[index] == 'A':
        temp = cups[0]
        cups[0] = cups[1]
        cups[1] = temp
    #input B swaps cup 2 with cup 3
    elif string_of_moves[index] == 'B':
        temp = cups[1]
        cups[1] = cups[2]
        cups[2] = temp
    #input C swaps cup 1 with cup 3
    elif string_of_moves[index] == 'C':
        temp = cups[0]
        cups[0] = cups[2]
        cups[2] = temp

#after exiting the loop, all swaps have been made: the cup containing the ball is identified by its truth label
for index in range(len(cups)):
    if cups[index]:
        print(index + 1)
