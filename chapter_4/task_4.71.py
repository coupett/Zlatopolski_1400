import math
alpha = float(input())
v0 = float(input())
P = float(input())
R = float(input())
H = float(input())
g = 9.8
alpha_rad = alpha * math.pi / 180
t = R / (v0 * math.cos(alpha_rad))
y = v0 * t * math.sin(alpha_rad) - g * t * t / 2
if H <= y <= H + P:
    print("поразит")
else:
    print("не поразит")