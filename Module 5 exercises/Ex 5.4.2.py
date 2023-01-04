# Создать генератор цикла, то есть в функцию, на входе будет передаваться массив, например, [1, 2, 3],
# генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.
def gen_cycle(arr):
    arr_values = arr.copy()
    while arr_values:
        value = arr_values.pop(0)
        arr_values.append(value)
        yield value


for num in gen_cycle([1, 2, 3]):
    print(num)
