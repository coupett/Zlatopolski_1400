n = int(input())
temp = n
reverse_num = 0
while temp > 0:
    digit = temp % 10
    reverse_num = reverse_num * 10 + digit
    temp //= 10

if n == reverse_num:
    print("является палиндромом")
else:
    print("не является палиндромом")