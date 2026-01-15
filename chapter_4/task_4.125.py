weight = float(input())
if weight < 60:
    print("легкий вес")
elif weight < 64:
    print("первый полусредний вес")
elif weight < 69:
    print("полусредний вес")
else:
    print("вес выше категории")