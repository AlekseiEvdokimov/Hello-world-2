# С помощью рекурсивной функции развернуть строку.
def rec_str(s):
    i = len(s)
    # print(s)
    if i == 0:
        return ""
    return s[-1] + rec_str(s[:-1])


print(rec_str('кот'))
