k = int(input())
num1, num2 = 1, 2
den1, den2 = 1, 1
if k == 1:
    print(num1, '/', den1)
elif k == 2:
    print(num2, '/', den2)
else:
    for i in range(3, k + 1):
        num = num1 + num2
        den = den1 + den2
        num1, num2 = num2, num
        den1, den2 = den2, den
    print(num, '/', den)