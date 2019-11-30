import sys

first = sys.stdin.readline().strip().split(" ")
n = int(first[0])
m = int(first[1])

#convert the string to lowercase
peek = sys.stdin.readline().strip().lower()
full = sys.stdin.readline().strip().lower()

#decoded string
final = list(' ' * (m - n))

#add the peeked letters
for letter in peek:
    final.append(letter)

for i in range(m - 1, n - 1, -1):
    # decode each letter based on k(n+i) = a(i)
    # we can deduce each k(i) since k(i) = (b(i) - a(i) mod 26)
    final[i-n] = chr(97 + (ord(full[i]) - ord(final[i])) % 26)
decoded = "".join((final))
print(decoded)