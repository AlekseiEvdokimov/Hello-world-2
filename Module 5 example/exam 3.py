def pow_func(base, n=2):
   print(base ** n)
   return None

print(pow_func(3))
# 9
# None
print("\n Или \n")


def pow_func2(base, n=2):
    inside_result2 = base ** n
    return inside_result2

print(pow_func2(3))
# 9