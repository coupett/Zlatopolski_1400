n = int(input())
temp = n
position = 0
found_position = 0

while temp > 0:
    position += 1
    digit = temp % 10
    if digit == 3:
        found_position = position
    temp //= 10

print(found_position)