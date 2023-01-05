# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора.
def my_decorator(fn):
    # print("Этот код будет выведен один раз в момент декорирования функции")
    n = 0

    def wrapper(*args, **kwargs):
        nonlocal n
        # print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        # print('Этот код будет выполняться после каждого вызова функции')
        n += 1
        print(n)
        return result

    return wrapper


@my_decorator
def say_word(word):
    print(word)


for i in range(10):
    say_word("Oo!!!")
