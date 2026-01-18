n = int(input())
b = int(input())
x = list(map(int, input().split()))
print(sum(x) % b == 0)