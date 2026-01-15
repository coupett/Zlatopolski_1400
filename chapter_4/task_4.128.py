a = float(input())
b = float(input())
c = float(input())
maxi = a
mini = a
if b > maxi:
    maxi = b
if c > maxi:
    maxi = c
if b < mini:
    mini = b
if c < mini:
    mini = c
print(maxi, mini)