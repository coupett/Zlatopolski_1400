n = int(input())
a = int(input())
b = int(input())

temp = n
pos_a = -1
pos_b = -1
index = 0

while temp > 0:
    digit = temp % 10
    if digit == a:
        pos_a = index
    if digit == b:
        pos_b = index
    temp //= 10
    index += 1

if pos_a != -1 and pos_b != -1:
    if pos_a < pos_b:
        print(a)
    else:
        print(b)
else:
    print("нет обеих цифр")