a2 = int(input())
a1 = int(input())
b = int(input())
if a1 >= b:
    des = a2
    ed = a1 - b
else:
    des = a2 - 1
    ed = a1 + 10 - b
print(des)
print(ed)