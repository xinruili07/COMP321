import sys

fullstring = sys.stdin.readline().strip().split(" ")
div1 = int(fullstring[0])
div2 = int(fullstring[1])
limit = int(fullstring[2])

for index in range(1, limit+1):
    # if divisible by both divisor
    if (index%div1 == 0 and index%div2 == 0):
        print("FizzBuzz")
    # if only divisible by first divisor
    elif (index%div1 == 0):
        print("Fizz")
    #if only divisible by second divisor
    elif (index%div2 == 0):
        print("Buzz")
    #if divisible by neither divisor
    else:
        print(index)