S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число

# заводим цикл while, который будет работать, пока сумма не превысит 500
while S < 500:  # делай пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счётчик
    print("Ещё считаю ...")

print("Сумма равна: ", S)
print("Количество чисел: ", n)