n = int(input())

# а) n-й член Фибоначчи
if n == 1 or n == 2:
    fib = 1
else:
    f1, f2 = 1, 1
    for i in range(3, n + 1):
        fib = f1 + f2
        f1, f2 = f2, fib
print(fib)

# б) первые n членов Фибоначчи
if n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    f1, f2 = 1, 1
    print(1, 1, end=' ')
    for i in range(3, n + 1):
        fib = f1 + f2
        print(fib, end=' ')
        f1, f2 = f2, fib
print()