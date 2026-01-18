n = int(input())
a = list(map(float, input().split()))
sum_squares = 0
for num in a:
    sum_squares += num**2
print(sum_squares)