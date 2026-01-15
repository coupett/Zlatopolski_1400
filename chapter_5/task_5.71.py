import math
result = math.sqrt(50)
for i in range(49, 0, -1):
    result = math.sqrt(i + result)
print(result)