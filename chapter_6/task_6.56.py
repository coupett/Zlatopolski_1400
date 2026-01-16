n = int(input())
temp = n
pos_2 = -1
pos_5 = -1
index = 0

digits = []
while temp > 0:
    digits.append(temp % 10)
    temp //= 10

digits = digits[::-1]
for i in range(len(digits)):
    if digits[i] == 2 and pos_2 == -1:
        pos_2 = i
    if digits[i] == 5 and pos_5 == -1:
        pos_5 = i

if pos_2 != -1 and pos_5 != -1:
    if pos_2 < pos_5:
        print("2 левее")
    else:
        print("5 левее")
else:
    print("нет обеих цифр")