# Вариант 1: с условным оператором
for i in range(10, 101):
    if i % 2 == 1:
        print(i, end=' ')
print()

# Вариант 2: без условного оператора
for i in range(11, 101, 2):
    print(i, end=' ')