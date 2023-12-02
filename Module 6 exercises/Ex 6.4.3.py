# a*x**2 + b*x + c = 0 - общий вид уравнения
# Напишите функцию D(a,b,c), возвращающую дискриминант квадратного уравнения.
def discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    return D


def quadratic_solve(a, b, c):
    D = discriminant(a, b, c)
    if D < 0:
        return "Нет вещественных корней"
    elif D > 0:
        x1 = (-b - D**0.5)/(2*a)
        x2 = (-b + D**0.5)/(2*a)
        return x1, x2
    else:
        x = -b / (2 * a)
        return x


print(quadratic_solve(2, 2, 2))
print(quadratic_solve(1, -4, 4))
print(quadratic_solve(1, 3, -4))

print(type(quadratic_solve(2, 2, 2)))
print(type(quadratic_solve(1, -4, 4)))
print(type(quadratic_solve(1, 3, -4)))