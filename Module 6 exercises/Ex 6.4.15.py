# Реализуйте функцию-декоратор,
# которая проверяет доступ к функции по username пользователя.
# Все username пользователей хранятся в глобальной области видимости в списке USERS.
# При согласии пользователя на авторизацию ему предлагается ввести username,
# который также хранится в глобальной области видимости.
# Функция должна использовать два декоратора: один для проверки авторизации вообще (реализован выше),
# второй — для проверки доступа.



yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"


def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper


USERS = ['admin', 'guest', 'director', 'root', 'superstar']




def has_access(func):
    auth2 = username in USERS
    def wrapper():
        if auth2:
            print("Пользователь верефицирован")
            func()
        else:
            print("Пользователь неверефицирован.")
    return wrapper


if auth:
    username = input("Введите ваш username:")

@is_auth
@has_access
def from_db():
    print("some data from database")


from_db()

