import sys

i = 0
number, capacity, difference = 0, 0, 0

socks = []
for line in sys.stdin:
    if (i == 0):
        line = line.strip()
        test_list = line.split()
        number = int(test_list[0])
        capacity = int(test_list[1])
        difference = int(test_list[2])
        i += 1
    elif (i == 1):
        line.strip()
        for item in line.split():
            socks.append(int(item))
        break

socks.sort()
numberMachines = 1
numberSocksInMachine = 1
lowestColorInMachine = socks[0]

for index in range(1, number):
    if (numberSocksInMachine == capacity):
        numberMachines += 1
        numberSocksInMachine = 0
        lowestColorInMachine = socks[index]

    if ((socks[index] - lowestColorInMachine) > difference):
        numberMachines += 1
        numberSocksInMachine = 0
        lowestColorInMachine = socks[index]

    numberSocksInMachine += 1

print(numberMachines)






