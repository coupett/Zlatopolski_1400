numbers = []
while True:
    num = int(input())
    if num < 0:
        break
    numbers.append(num)

if numbers:
    average = sum(numbers) / len(numbers)
    print(average)
else:
    print("Нет чисел")