# Напишите рекурсивную функцию, которая зеркально разворачивает число. Предполагается, что число не содержит нули.
# без рекурсии
def reverseNum(L):
    x = list(map(int, str(L)))
    rev = int(''.join(map(str, x[::-1])))
    return rev


# с рекурсией
def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res


L = 999454872111
#print(L)
print(reverseNum(L))
print(mirror(L))
