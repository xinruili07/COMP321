import sys

numberOfBus = int(sys.stdin.readline().strip())
stringBus = sys.stdin.readline().strip().split()
intBus = []
for bus in stringBus:
    intBus.append(int(bus))

intBus.sort()

index = 0
string = ""
while index < numberOfBus:
    first = intBus[index]
    while (index + 1 < numberOfBus and intBus[index] + 1 == intBus[index+1]):
        index += 1
    last = intBus[index]
    if (first == last):
        string += "{} ".format(last)
    elif (first + 1== last):
        string += "{} {} ".format(first, last)
    else:
        string += "{}-{} ".format(first, last)
    index += 1

print(string)