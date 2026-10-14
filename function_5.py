def converter_rome(n):

    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    result = ""
    for value, rome_value in values:
        while n >= value:
            result += rome_value
            n -= value
    return result
def converter_int(s):

    rome_values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    result = 0
    for i in range(len(s)):
        if i < len(s) - 1 and rome_values[s[i]] < rome_values[s[i + 1]]:
            result -= rome_values[s[i]]
        else:
            result += rome_values[s[i]]
    return result
a = input("Выберите действие:\n1. Обычное число → римское\n2. Римское число → обычное\n0. Выход\n\nВаш выбор: ")
if a == "1":
    print(converter_rome(int(input("введите арабское число "))))
elif a == "2":
    print(converter_int(int(input("введите римское число "))))
else:
    print("Некорректный ввод")


