n = int(input())
f1, f2 = 1, 1
sum_fib = 2  # сумма первых двух чисел
for i in range(3, n+1):
    fib = f1 + f2
    sum_fib += fib
    f1, f2 = f2, fib
if sum_fib % 2 == 0:
    print("сумма четная")
else:
    print("сумма нечетная")