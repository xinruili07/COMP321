import sys

menuLength = int(sys.stdin.readline().strip())
menuItems = sys.stdin.readline().strip().split(' ')
orderLength = int(sys.stdin.readline().strip())
orderItems = sys.stdin.readline().strip().split(' ')

# given 1 <= m <= 1000, given 1 <= s <= 30000
ready = ["Impossible"] * 100000
ready[0] = 0

for i in range(menuLength):
    menuItem = int(menuItems[i])
    for j in range(30000):
        if isinstance(ready[j], int):
            if ready[j] >= 0:
                if ready[j + menuItem] == "Impossible":
                    ready[j+menuItem] = i
                else:
                    ready[j+menuItem] = "Ambiguous"
        
        if ready[j] == "Ambiguous":
            ready[j + menuItem] = "Ambiguous"


# If there is one unique order giving the specified total cost, output a space-separated list of the numbers of the items.
# If the order contains more than one of the same item, print the corresponding number the appropriate number of times.
# If there doesn’t exist an order that gives the specified sum, output Impossible.
# If there are more than one order that gives the specified sum, output Ambiguous.
for i in orderItems:
    orderItem = int(i)
    if ready[orderItem] == "Impossible":
        print("Impossible")
    elif ready[orderItem] == "Ambiguous":
        print("Ambiguous")
    else:
        ITEMS = []
        while (orderItem > 0):
            ITEMS.append(int(ready[orderItem])+1)
            orderItem -= int(menuItems[ready[orderItem]])
        ITEMS.sort()
        itemString = ""
        for item in ITEMS:
            itemString += str(item) + " "
        print(itemString)
