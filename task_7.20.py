capacity = float(input())
masses = list(map(float, input().split()))
total = sum(masses)
print(total <= capacity)