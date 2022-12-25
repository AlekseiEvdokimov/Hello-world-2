L = ["а", "б", "в", 1, 2, 3, 4]
print (L[:3:-1])
# [4, 3, 2]


string ='1 1 2 3 5 8 13 21 34 55'

list_of_strings = string.split() # список строковых представлений чисел
L = list(map(int, list_of_strings)) # cписок чисел
L[0], L[-1] = L[-1], L[0]
L.append(sum(L))
print(L)