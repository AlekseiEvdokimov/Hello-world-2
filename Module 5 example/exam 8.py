def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обёртку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, который будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")

        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result

    return wrapper

"""ПРИМЕР"""
def my_function():
   print("Я - оборачиваемая функция!")
   return 0

print(my_function())
# Я оборачиваемая функция!
# 0

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
# Я буду выполнен до основного вызова!
# Я оборачиваемая функция!
# Я буду выполнен после основного вызова!
# 0