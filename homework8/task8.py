import random
# Лотерейный билет
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
# Выбор пользователя
u_choice = []
for i in range(5):
    print(f"Выберите число из строки {i+1}: {ticket[i]}")
    while True:
        try:
            choice = int(input())
            if choice in ticket[i]:
                u_choice.append(choice)
                break
            else:
                print("Некорректный ввод. Введите число из текущей строки.")
        except ValueError:
            print("Некорректный ввод. Введите число.")

# Выбор программы
p_choice = []
for i in range(5):
    p_choice.append(random.choice(ticket[i]))

# Статистика
print("\nВаши выбранные числа:", u_choice)
print("Числа, выбранные программой:", p_choice)

# Сравнение выбора
ns = []
for n in u_choice:
    if n in p_choice:
        ns.append(n)
print(f"Совпадений: {len(ns)}")
print(f"Совпадающие числа: ", ns)

