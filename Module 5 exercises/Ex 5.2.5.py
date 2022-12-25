#Напишите функцию, которая будет возвращать количество делителей числа а.
def dev_a(a):
    devs = 0
    for i in range(1, a+1):
        if a % i == 0:
            devs +=1
    return devs


a = int(input("Введите число: "))
print("Число делителей: ", dev_a(a))
