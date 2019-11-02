import sys

before = list(sys.stdin.readline().strip())
after = list(sys.stdin.readline().strip())


# Remove identical items from the beginning of each list
while (len(before) > 0 and len(after) > 0 and before[0] == after[0]):
    before.pop(0)
    after.pop(0)

# Remove identical items from the end of each list
while (len(before) > 0 and len(after) > 0 and before[-1] == after[-1]): 
    before.pop()
    after.pop()

# print the length of what remains
print(len(after))