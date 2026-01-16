import math
a = int(input())
b = int(input())

# а) с предусловием
i = a
while i >= b:
    print(math.sqrt(i))
    i -= 1

# б) с постусловием
i = a
while True:
    print(math.sqrt(i))
    i -= 1
    if i < b:
        break