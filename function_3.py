def print_pack_report(n):
    if n <= 1:
        print("Некорректное число")
    for i in range(n, 1, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - расфасуем по 3 или по 5")
            continue
        if i % 3 == 0 and i % 5 != 0:
            print(f"{i} - расфасуем по 3")
            continue
        if i % 5 == 0 and i % 3 != 0:
            print(f"{i} - расфасуем по 5")
            continue
        if i % 5 != 0 and i % 3 != 0:
            print(f"{i} - не заказываем")
            continue
print_pack_report(int(input("Введите целое число пирожных(больше единицы) ")))


