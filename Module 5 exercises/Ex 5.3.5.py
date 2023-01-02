# Дано натуральное число N. Вычислите сумму его цифр.
def rec_sum_n(n):
    if n//10 == 0:
        return n
    return n%10 + rec_sum_n(n//10)

print(rec_sum_n(12))
