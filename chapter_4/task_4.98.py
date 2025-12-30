n = int(input())
a = int(input())
summa = 0
for i in range(n):
    summa += a + i
if summa % 2 == 0:
    print("четная")
else:
    print("нечетная")