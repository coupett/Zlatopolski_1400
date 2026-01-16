# a) f(x) = x^4 + 2x^3 - x - 1, a=0, b=1
a, b = 0, 1
for _ in range(1000):
    mid = (a + b) / 2
    f_mid = mid**4 + 2*mid**3 - mid - 1
    f_a = a**4 + 2*a**3 - a - 1

    if f_mid == 0 or (b - a) < 0.001:
        break

    if f_a * f_mid < 0:
        b = mid
    else:
        a = mid

print("а) Приближенный корень:", round((a + b) / 2, 3))

# б) f(x) = x^3 - 0.2x^2 - 0.2x - 1.2, a=1, b=1.5
a, b = 1, 1.5
for _ in range(1000):
    mid = (a + b) / 2
    f_mid = mid**3 - 0.2*mid**2 - 0.2*mid - 1.2
    f_a = a**3 - 0.2*a**2 - 0.2*a - 1.2

    if f_mid == 0 or (b - a) < 0.001:
        break

    if f_a * f_mid < 0:
        b = mid
    else:
        a = mid

print("б) Приближенный корень:", round((a + b) / 2, 3))