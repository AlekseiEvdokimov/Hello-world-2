# a*x**2 + b*x + c = 0 - общий вид уравнения
# Напишите функцию D(a,b,c), возвращающую дискриминант квадратного уравнения.
def discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    return D


print(discriminant(2, 2, 2))
print(discriminant(1, -4, 4))
print(discriminant(1, 3, -4))
