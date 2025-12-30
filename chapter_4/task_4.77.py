def ugroza(fig, x1, y1, x2, y2):
    if fig == "ладья":
        return x1 == x2 or y1 == y2
    elif fig == "слон":
        return abs(x1 - x2) == abs(y1 - y2)
    elif fig == "ферзь":
        return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)
    elif fig == "конь":
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
    elif fig == "король":
        return max(abs(x1 - x2), abs(y1 - y2)) == 1
    else:
        return False

def hod(fig, x1, y1, x2, y2):
    if fig == "пешка":
        return False
    else:
        return ugroza(fig, x1, y1, x2, y2)

white = input()
black = input()
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if hod(white, a, b, e, f) and not ugroza(black, c, d, e, f):
    print("может")
else:
    print("не может")