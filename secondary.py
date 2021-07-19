# -------------------- Section 2 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   b. Prompt input from the user in the form of an integer. Save to a variable named size.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#   >> size... 4
#
#   $$$$
#    $$$
#     $$
#      $
#
# Write Code Below #

size = int(input('Enter a size :D : '))
s = input('Enter a symbol :D : ')
for i in range(size):
    print(' ' * i + s * (size - i))


# 2 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#
#
# Write Code Below #
s = input('Enter the symbol :D: ')
num = int(input('Enter the number: '))
start = -num
end = num
step = 1
for i in range(start, end, step):
    print(s * (abs(i) + 1))

# 3 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using two for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#
#
# Write Code Below #
s = input('Enter a symbol: ')

for i in range(6):
    print(s * i)

for i in range(4):
    print(s * (4 - i))


# ---------- Part 2 | Mathematical Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 2\n'
)

# 1 - for Loop | Sum n
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate the sum of all numbers between 0 and n, and print the value.
#
#   sum = n + n - 1 + n - 2 + n - 3
#
#   EXAMPLE: 5 --> 5 + 4 + 3 + 2 + 1
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #
n = int(input('Please enter a number '))

for i in range(0, n):
    n = n + i

print(n)

# 1 - for Loop | n!
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate n! using loops.
#
#   n! or n factorial is equal to n * (n - 1) * (n - 2) * ... * 1
#
#   EXAMPLE: 5 --> 5 * 4 * 3 * 2 * 1
#
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #
n = int(input('Please enter a number '))

for i in range(1, n + 1):
    n = n * i

print(n)