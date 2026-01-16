# a) год, когда урожайность > 22 ц/га
urozh = 20
year = 1
while urozh <= 22:
    year += 1
    urozh *= 1.02
print("Год:", year)

# б) год, когда площадь > 120 га
plosh = 100
year = 1
while plosh <= 120:
    year += 1
    plosh *= 1.05
print("Год:", year)

# в) год, когда общий урожай > 800 ц
plosh = 100
urozh = 20
total = 0
year = 1
while total <= 800:
    total += plosh * urozh
    year += 1
    plosh *= 1.05
    urozh *= 1.02
print("Год:", year - 1)