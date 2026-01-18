sportsman1 = list(map(int, input().split()))
sportsman2 = list(map(int, input().split()))
total1 = sum(sportsman1)
total2 = sum(sportsman2)
if total1 > total2:
    print("Первый спортсмен")
else:
    print("Второй спортсмен")