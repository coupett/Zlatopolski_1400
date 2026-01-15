import math
r = 5  # внутренний радиус в см
thick = 0.5  # толщина в см
total_volume = 0
for i in range(12):
    volume = 4/3 * math.pi * (r ** 3)
    total_volume += volume
    r += thick
# Переводим из см³ в литры (1 л = 1000 см³)
total_volume_liters = total_volume / 1000
print(total_volume_liters)