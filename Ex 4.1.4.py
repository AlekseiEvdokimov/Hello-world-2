year_ves = int(input("Введите год :"))
print((year_ves % 400 == 0) or (( year_ves % 4 == 0) and ( year_ves % 100 != 0)))