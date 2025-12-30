t = float(input())
t = t % 6
if t < 3:
    print("зеленый")
elif t < 4:
    print("желтый")
else:
    print("красный")