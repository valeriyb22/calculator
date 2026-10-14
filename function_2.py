def check_winners(scores, student):
    scores = sorted(scores)
    best_3 = scores[-3:]
    if str(student) in best_3:
        return "Вы в тройке лидеров"
    else:
        return "Вы не в тройке лидеров"


print(check_winners(list(input("Введите список баллов участников ")), int(input("Введите свой балл "))))
