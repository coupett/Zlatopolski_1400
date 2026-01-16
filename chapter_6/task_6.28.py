num = 500
count = 0
while count < 20:
    if num % 13 == 0 or num % 17 == 0:
        print(num)
        count += 1
    num += 1