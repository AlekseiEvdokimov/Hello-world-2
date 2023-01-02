# Написать функцию, которая будет перемножать любое количество переданных ей аргументов.
def adder(*nums):
    sum_ = 1
    for n in nums:
        # print(n)
        # print("nums: ", nums)
        sum_ *= n

    return sum_


print(adder(1, 2, 7))  # 6
