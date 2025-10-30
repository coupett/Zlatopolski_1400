#S = π * R² - π * r²
import math
r = int(input())
R = int(input())
S = math.pi * (R*R - r*r)
print(S)