import sys

def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

fullstring = sys.stdin.readline().strip().split(" ")
integer1 = fullstring[0]
integer2 = fullstring[1]
limit = fullstring[2]

lcm = compute_lcm(int(integer1), int(integer2))
if  (lcm <= int(limit)):
    print("yes")
else:
    print("no")