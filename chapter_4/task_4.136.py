# 1) год не високосный
month = int(input())
if month == 2:
    print("28 дней")
elif month in [4, 6, 9, 11]:
    print("30 дней")
else:
    print("31 день")

# 2) год может быть високосным
month = int(input())
vis = int(input())  # 1 - високосный, 0 - не високосный
if month == 2:
    if vis == 1:
        print("29 дней")
    else:
        print("28 дней")
elif month in [4, 6, 9, 11]:
    print("30 дней")
else:
    print("31 день")