import sys

fullstring = sys.stdin.readline().strip().split(" ")
type = fullstring[0]
string1 = fullstring[1]

if type == "E":
    finalstring = ""
    counter = 1
    finalstring += string1[1]

    for index in range(len(string1)-1):
        if string1[index] == string1[index+1]:
            counter += 1
        else:
            finalstring += str(counter)
            finalstring += string1[index+1]
            counter = 1
    finalstring += str(counter)
    print(finalstring)

if type == "D":
    finalstring = ""
    for index, digit in enumerate(string1):
        if digit.isdigit():
            finalstring += (int(digit) * string1[index-1])
    print(finalstring)
