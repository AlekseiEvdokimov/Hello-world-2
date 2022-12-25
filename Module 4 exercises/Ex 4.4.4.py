"""
Напишите программу, которая сначала запрашивает логин пользователя, проверяет, существует он или нет, а
 потом с помощью вложенного условия проверяет пароль этого пользователя.

 login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123'
}

username = input('Введите логин:\n')

# здесь допишите условие проверки логина и пароля

"""

login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123'
}

#print(login_list)
username = input('Введите логин:\n')

if username in login_list:
    print("Лгоин найден!")
    password = input('Введите пароль:\n')
    #print(password_list[username])
    if password == password_list[username]:
       print("Пароль верный!")
    else:
       print("Пароль НЕверный!")

else:
   print("Лгоин НЕ найден!")
