n = int(input())
yarus = (n - 1) // 120 + 1
sekciya = ((n - 1) % 120) // 15 + 1
print(sekciya)
print(yarus)

n = int(input())
sekciya = (n - 1) // 150 + 1
yarus = ((n - 1) % 150) // 15 + 1
print(sekciya)
print(yarus)