import math

n = int(input())

# а)
sum_sin = 0
total_a = 0
for i in range(1, n + 1):
    sum_sin += math.sin(i)
    total_a += 1 / sum_sin
print(total_a)

# б)
result_b = math.sqrt(2)
for i in range(2, n + 1):
    result_b = math.sqrt(2 + result_b)
print(result_b)

# в)
sum_cos = 0
sum_sin = 0
total_c = 0
for i in range(1, 2*n + 1):
    sum_cos += math.cos(i)
    sum_sin += math.sin(i)
    if i % 2 == 0:
        total_c += sum_cos / sum_sin
print(total_c)

# г)
result_d = math.sqrt(3*n)
for i in range(n-1, 0, -1):
    result_d = math.sqrt(3*i + result_d)
print(result_d)