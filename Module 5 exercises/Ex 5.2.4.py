def revers_star(n):
    for i in range(1, n + 1):
        print("*" * n)
        n -= 1


n = int(input("Введите число: "))
revers_star(n)

"""
def reverse_stair(n):
   for i in range(n, 0, -1):
       print("*" * i)

reverse_stair(5)"""
