import math
y = float(input())
total_minutes = y * 360 / math.pi
hours = int(total_minutes // 60)
minutes = int(total_minutes % 60)
angle_minute = (total_minutes % 60) * math.pi / 30
print(angle_minute)
print(hours % 12)
print(minutes)