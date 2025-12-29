a = float(input())
b = float(input())
c = float(input())
d = float(input())
if (c + 2 <= a and d + 2 <= b) or (c + 2 <= b and d + 2 <= a):
    print("войдет")
else:
    print("не войдет")