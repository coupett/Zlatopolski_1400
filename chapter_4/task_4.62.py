a = float(input())
b = float(input())
c = float(input())
d = float(input())
if (a <= c and b <= d) or (a <= d and b <= c):
    print("можно")
else:
    print("нельзя")