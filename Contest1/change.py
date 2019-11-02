import sys

nbCases = int(sys.stdin.readline().strip())
cases = []

for i in range(nbCases):
    cases.append(int(sys.stdin.readline().strip()))

nbChange = int(sys.stdin.readline().strip())
changes = []
for i in range(nbChange):
    changes.append(int(sys.stdin.readline().strip()))

changes.sort(reverse=True)

for case in cases:
    i = 0
    changeAnswer = []
    while(i < len(changes)): 
        while (case >= changes[i]): 
            case -= changes[i] 
            changeAnswer.append(changes[i])
        i += 1
    if sum(changeAnswer) < case:
        list = [sum(changeAnswer.append(change)) - case for change in changes]
        index = list.index(min(list))
        changeAnswer.append(changes[index])
        
    print(str(sum(changeAnswer)) + " " + str(len(changeAnswer)))