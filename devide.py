def divide(a, b):
    if b == 0:
        return "Ошибка: на ноль делить нельзя"
    return a / b


result = divide(10, 0)
print(f"Результат: {result}")
