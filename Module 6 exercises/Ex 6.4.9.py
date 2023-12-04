# Напишите рекурсивную функцию, находящую минимальный элемент списка без использования циклов
# и встроенной функции min().
def recMinList(x):
    if len(x) > 1:
        if x[0] < x[1]:
            x = list(x)
            x.pop(1)
            return recMinList(x)
        else:
            x = list(x)
            x.pop(0)
            return recMinList(x)
    else:
        return x[0]


def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])


L = [1, 3, -4, 5]
print(type(L))
print(min_list(L))
print(recMinList(L))
