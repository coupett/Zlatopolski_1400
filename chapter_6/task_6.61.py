n = int(input())
temp = n
digits = []
pos = 0

while temp > 0:
    digit = temp % 10
    digits.append((digit, pos + 1))
    temp //= 10
    pos += 1

digits_sorted = sorted(digits, key=lambda x: x[0], reverse=True)
max1_val, max1_pos_end = digits_sorted[0]
max2_val, max2_pos_end = digits_sorted[1]

digits_rev = []
temp = n
while temp > 0:
    digits_rev.append(temp % 10)
    temp //= 10
digits_rev = digits_rev[::-1]

for i in range(len(digits_rev)):
    if digits_rev[i] == max1_val:
        max1_pos_start = i + 1
    if digits_rev[i] == max2_val:
        max2_pos_start = i + 1

print("а) от конца:", max1_pos_end, max2_pos_end)
print("   от начала:", max1_pos_start, max2_pos_start)

min1_val, min1_pos_end = digits_sorted[-1]
min2_val, min2_pos_end = digits_sorted[-2]

for i in range(len(digits_rev)):
    if digits_rev[i] == min1_val:
        min1_pos_start = i + 1
    if digits_rev[i] == min2_val:
        min2_pos_start = i + 1

print("б) от конца:", min1_pos_end, min2_pos_end)
print("   от начала:", min1_pos_start, min2_pos_start)