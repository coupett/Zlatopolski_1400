month = int(input())
if month in [12, 1, 2]:
    print("зима")
elif month in [3, 4, 5]:
    print("весна")
elif month in [6, 7, 8]:
    print("лето")
elif month in [9, 10, 11]:
    print("осень")
else:
    print("некорректный номер месяца")