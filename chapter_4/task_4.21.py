x1 = float(input())
y1 = float(input())
w1 = float(input())
h1 = float(input())
x2 = float(input())
y2 = float(input())
w2 = float(input())
h2 = float(input())
x1r = x1 + w1
y1r = y1 + h1
x2r = x2 + w2
y2r = y2 + h2
xl = min(x1, x2)
yl = min(y1, y2)
xr = max(x1r, x2r)
yr = max(y1r, y2r)
print(xl)
print(yl)
print(xr)
print(yr)