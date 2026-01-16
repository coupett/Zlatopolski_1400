n = int(input())
temp = n
position = 0
found_position = 0
count = 0

while temp > 0:
    position += 1
    digit = temp % 10
    if digit == 8:
        found_position = position
        count += 1
    temp //= 10

if count == 0:
    print(0)
else:
    print(found_position)