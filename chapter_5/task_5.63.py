result = 20 * 20
for i in range(19, 0, -1):
    result = (result - i * i) ** 2
print(result)