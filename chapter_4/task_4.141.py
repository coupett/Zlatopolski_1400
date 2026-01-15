# a) 1 января - понедельник
k = int(input())
day = (k - 1) % 7
if day == 0:
    print("понедельник")
elif day == 1:
    print("вторник")
elif day == 2:
    print("среда")
elif day == 3:
    print("четверг")
elif day == 4:
    print("пятница")
elif day == 5:
    print("суббота")
elif day == 6:
    print("воскресенье")

# б) 1 января - d-й день недели
k = int(input())
d = int(input())
day = (k - 1 + d - 1) % 7
if day == 0:
    print("понедельник")
elif day == 1:
    print("вторник")
elif day == 2:
    print("среда")
elif day == 3:
    print("четверг")
elif day == 4:
    print("пятница")
elif day == 5:
    print("суббота")
elif day == 6:
    print("воскресенье")