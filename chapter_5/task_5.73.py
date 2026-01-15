import math
l = 4.5
x = 3.0
while x > 0:
    cos_angle = x / l
    angle = math.degrees(math.acos(cos_angle))
    print(f"При x={x:.1f} м, угол={angle:.1f}°")
    x -= 0.2