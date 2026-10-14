from calculator import add_numbers


def test_add_numbers():
    result = add_numbers(2.5, 3.5)
    if result == 6.0:
        print(" Тест 1 пройден: 2.5 + 3.5 = 6.0")
    else:
        print(f" Тест 1 провален: ожидали 6.0, получили {result}")
        result = add_numbers(-1.0, 1.0)
    if result == 0.0:
        print("Тест 2 пройден: -1.0 + 1.0 = 0.0")
    else:
        print(f"Тест 2 провален: ожидали 0.0, получили {result}")
    result = add_numbers(0.0, 0.0)
    if result == 0.0:
        print("Тест 3 пройден: 0.0 + 0.0 = 0.0")
    else:
        print(f"Тест 3 провален: ожидали 0.0, получили {result}")


test_add_numbers()
