password = 12345
user_pass = int(input("Введите пароль: "))
while user_pass != password:
    print("Неверный пароль!")
    user_pass = int(input("Введите пароль: "))
print("Добро пожаловать!")