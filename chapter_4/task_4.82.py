n = int(input())
if 10 <= n % 100 <= 20:
    slovo = "лет"
elif n % 10 == 1:
    slovo = "год"
elif 2 <= n % 10 <= 4:
    slovo = "года"
else:
    slovo = "лет"
print("мне", n, slovo)