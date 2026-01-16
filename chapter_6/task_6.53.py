n = int(input())
a = int(input())
b = int(input())
k = int(input())
a2 = int(input())
b3 = int(input())

temp = n
count_a = 0
has_a = False
has_b = False

while temp > 0:
    digit = temp % 10
    if digit == a:
        count_a += 1
        has_a = True
    if digit == b:
        has_b = True
    temp //= 10

print("а)", has_a)
print("б)", not has_b)
print("в)", count_a > k)

temp = n
has_a2 = False
has_b3 = False
while temp > 0:
    digit = temp % 10
    if digit == a2:
        has_a2 = True
    if digit == b3:
        has_b3 = True
    temp //= 10
print("г)", has_a2 and has_b3)