# a) день, когда пробежит больше 20 км
probeg = 10
day = 1
while probeg <= 20:
    day += 1
    probeg *= 1.1
print("День:", day)

# б) день, когда суммарный пробег превысит 100 км
probeg = 10
total = 10
day = 1
while total <= 100:
    day += 1
    probeg *= 1.1
    total += probeg
print("День:", day)