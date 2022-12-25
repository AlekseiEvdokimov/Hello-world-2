#Напишите функцию, которая будет возвращать количество делителей числа а.
def dev_a(a):
    devs = 0
    for i in range(1, a+1):
        if a % i == 0:
            devs +=1
    return devs


a = int(input("Введите число: "))
print("Число делителей: ", dev_a(a))

"""
Или

def get_multipliers(a):
   count = 1
   for n in range(1, a // 2 + 1):
       if a % n == 0:
           count += 1

   return count

get_multipliers(5)  # 2
get_multipliers(4)  # 3
"""