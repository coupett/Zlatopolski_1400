a = int(input())
b = int(input())
if a % b == 0:
    print("b делитель a")
elif b % a == 0:
    print("a делитель b")
else:
    print("ни одно не является делителем другого")