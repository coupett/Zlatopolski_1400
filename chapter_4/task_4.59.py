a = float(input())
b = float(input())
c = float(input())
if a == b == c:
    print("да")
else:
    print("нет")
if a == b or a == c or b == c:
    print("да")
else:
    print("нет")