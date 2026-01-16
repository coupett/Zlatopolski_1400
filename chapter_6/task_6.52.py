n = int(input())
temp = n
has_3 = False
has_2 = False
has_5 = False

while temp > 0:
    digit = temp % 10
    if digit == 3:
        has_3 = True
    if digit == 2:
        has_2 = True
    if digit == 5:
        has_5 = True
    temp //= 10

print("а)", has_3)
print("б)", has_2 and has_5)