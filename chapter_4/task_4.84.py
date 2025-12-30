n = int(input())
r = n // 100
k = n % 100
if r % 10 == 1 and r % 100 != 11:
    slovo_r = "рубль"
elif 2 <= r % 10 <= 4 and not (10 <= r % 100 <= 20):
    slovo_r = "рубля"
else:
    slovo_r = "рублей"
if k % 10 == 1 and k % 100 != 11:
    slovo_k = "копейка"
elif 2 <= k % 10 <= 4 and not (10 <= k % 100 <= 20):
    slovo_k = "копейки"
else:
    slovo_k = "копеек"
if r == 0:
    print(k, slovo_k)
elif k == 0:
    print(r, slovo_r, "ровно")
else:
    print(r, slovo_r, k, slovo_k)