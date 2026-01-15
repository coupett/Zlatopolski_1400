a = int(input())
b = int(input())
c = int(input())

# a) самое большое
if a > b and a > c:
    print("первое самое большое")
elif b > a and b > c:
    print("второе самое большое")
elif c > a and c > b:
    print("третье самое большое")

# б) самое маленькое
if a < b and a < c:
    print("первое самое маленькое")
elif b < a and b < c:
    print("второе самое маленькое")
elif c < a and c < b:
    print("третье самое маленькое")

# в) среднее
if (b < a < c) or (c < a < b):
    print("первое среднее")
elif (a < b < c) or (c < b < a):
    print("второе среднее")
elif (a < c < b) or (b < c < a):
    print("третье среднее")