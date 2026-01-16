n = int(input())

# а) степень числа 3
temp = n
is_power_3 = True
if temp <= 0:
    is_power_3 = False
else:
    while temp > 1:
        if temp % 3 != 0:
            is_power_3 = False
            break
        temp //= 3

print("а)", is_power_3)

# б) степень числа 5
temp = n
is_power_5 = True
if temp <= 0:
    is_power_5 = False
else:
    while temp > 1:
        if temp % 5 != 0:
            is_power_5 = False
            break
        temp //= 5

print("б)", is_power_5)