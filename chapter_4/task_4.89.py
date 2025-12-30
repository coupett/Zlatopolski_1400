a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = int(input())
m = int(input())
start = a * 60 + b
end = c * 60 + d
t = n * 60 + m
if start <= t < end:
    print("будет")
else:
    print("не будет")