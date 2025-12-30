y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())
if y1 < y2:
    print("первый старше")
elif y1 > y2:
    print("второй старше")
else:
    if m1 < m2:
        print("первый старше")
    elif m1 > m2:
        print("второй старше")
    else:
        if d1 < d2:
            print("первый старше")
        elif d1 > d2:
            print("второй старше")
        else:
            print("ровесники")