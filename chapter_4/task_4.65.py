a = float(input())
b = float(input())
c = float(input())
x = float(input())
y = float(input())
if (a <= x and b <= y) or (a <= y and b <= x) or (a <= x and c <= y) or (a <= y and c <= x) or (b <= x and c <= y) or (b <= y and c <= x):
    print("пройдет")
else:
    print("не пройдет")