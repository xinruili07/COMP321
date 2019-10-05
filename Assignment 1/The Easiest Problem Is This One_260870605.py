import sys

# create a new list with all the cases
test_list = []
for line in sys.stdin:
   #removes new line and white spaces
   line = line.strip()
   #convertes the line to an integer and appends it to the list if it is not equal to zero
   n = int(line)
   if n != 0:
       test_list.append(n)

# function to calculate the sum of all digits of a number
def sum_of_digits(num):
    sum = 0
    while num > 0:
        d = num % 10
        num = num // 10
        sum += d
    return sum

# iterate through all the test cases
for number in test_list:
    i = 1
    while True:
        #breaks the loop when we find the first number that results in the appropriate sum of digits
        if sum_of_digits(i*number) == sum_of_digits(number):
            print(i)
            break
        i += 1