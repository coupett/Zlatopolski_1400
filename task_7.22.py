set1 = list(map(float, input().split()))
set2 = list(map(float, input().split()))
total1 = sum(set1)
total2 = sum(set2)
if total1 < total2:
    print("Первый набор")
else:
    print("Второй набор")