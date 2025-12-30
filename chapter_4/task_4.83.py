k = int(input())
if 10 <= k % 100 <= 20:
    slovo = "грибов"
elif k % 10 == 1:
    slovo = "гриб"
elif 2 <= k % 10 <= 4:
    slovo = "гриба"
else:
    slovo = "грибов"
print("мы нашли", k, slovo, "в лесу")