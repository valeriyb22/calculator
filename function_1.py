def shifr(string, n):
    en = "abcdefghijklmnopqrstuvwxyz"
    ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    new_string = ""
    if string[1] in en:
        for i in string:
            new_string += en[(en.index(i) + n) % len(en)]
    if string[1] in ru:
        for i in string:
            new_string += ru[(ru.index(i) + n) % len(ru)]
    return new_string
print(shifr(input("Введите строку "), int(input("Введите сдвиг(целое число) "))))




