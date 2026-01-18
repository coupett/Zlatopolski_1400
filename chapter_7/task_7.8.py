numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

print("а) Сумма:", sum(numbers))
print("б) Количество:", len(numbers))