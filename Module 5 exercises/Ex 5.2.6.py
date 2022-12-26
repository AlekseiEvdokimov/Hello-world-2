#Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет, и возвращает результат проверки.
def check_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False


print(check_palindrome("test"))  # False
print(check_palindrome("Кит на море не романтик"))  # True
