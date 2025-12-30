a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    aa = a * a
    bb = b * b
    cc = c * c
    if aa + bb == cc or aa + cc == bb or bb + cc == aa:
        print("прямоугольный")
    elif aa + bb > cc and aa + cc > bb and bb + cc > aa:
        print("остроугольный")
    else:
        print("тупоугольный")
else:
    print("не существует")

a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        vid = "равносторонний"
    elif a == b or a == c or b == c:
        vid = "равнобедренный"
    else:
        vid = "разносторонний"
    aa = a * a
    bb = b * b
    cc = c * c
    if aa + bb == cc or aa + cc == bb or bb + cc == aa:
        ugol = "прямоугольный"
    elif aa + bb > cc and aa + cc > bb and bb + cc > aa:
        ugol = "остроугольный"
    else:
        ugol = "тупоугольный"
    print(ugol, vid)
else:
    print("не существует")