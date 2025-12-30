a2 = int(input())
a1 = int(input())
b2 = int(input())
b1 = int(input())
if a1 >= b1:
    ed = a1 - b1
    z = 0
else:
    ed = a1 + 10 - b1
    z = 1
des = a2 - b2 - z
print(des)
print(ed)