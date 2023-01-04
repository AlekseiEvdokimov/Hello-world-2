# Пример замыкания функции
def add_x_func(x):
    def add_y_func(y):
        def add_z_func(z):
            print("x:", x)
            print("y:", y)
            print("z:", z)
            return x + y + z  # захват переменной "x" из nonlocal области

        return add_z_func  # возвращение функции в качестве результата

    return add_y_func


add_y = add_x_func(1)
add_z = add_y(2)
print(add_z(3))  #
