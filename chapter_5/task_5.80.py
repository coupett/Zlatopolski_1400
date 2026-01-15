n = int(input())
for num in range(10, 100):
    if num % n == 0 or num // 10 == n or num % 10 == n:
        print(num)