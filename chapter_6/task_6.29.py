num = 100
count = 0
while count < 10:
    if num % 10 == 7 and num % 9 == 0:
        print(num)
        count += 1
    num += 1