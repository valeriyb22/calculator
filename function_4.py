import random
import string


def generate_password():
    print("=" * 30)
    print("   ГЕНЕРАТОР ПАРОЛЕЙ")
    print("=" * 30)
    length = int(input("Введите длину пароля: "))

    use_lower = input("Использовать строчные буквы? (да/нет): ").lower() == "да"
    use_upper = input("Использовать заглавные буквы? (да/нет): ").lower() == "да"
    use_digits = input("Использовать цифры? (да/нет): ").lower() == "да"
    use_special = input("Использовать спецсимволы? (да/нет): ").lower() == "да"

    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        print("Ошибка: не выбрано ни одного типа символов!")
        return
    password = ""
    for i in range(length):
        password += random.choice(chars)

    print("=" * 30)
    print(f"Ваш пароль: {password}")
    print("=" * 30)


generate_password()
