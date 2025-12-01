n = int(input())
chasov = n // 3600
minut = (n % 3600) // 60
sekund = n % 60
print(chasov)
print(minut)
print(sekund)