a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("прямоугольный")
    else:
        print("не прямоугольный")
else:
    print("не существует")