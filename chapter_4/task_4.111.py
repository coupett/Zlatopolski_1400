a = int(input())
b = int(input())
c = int(input())
d = int(input())
count = 0
if a % 2 == 0:
    count += 1
if b % 2 == 0:
    count += 1
if c % 2 == 0:
    count += 1
if d % 2 == 0:
    count += 1
print(count)