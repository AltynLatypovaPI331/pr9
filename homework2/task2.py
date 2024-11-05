#Создание список квадратов целых чисел между a и b (включительно).
def sq_bet(a, b):
  # Преобразование чисел в целые
  a = int(a)
  b = int(b)
  # Меняем местами, если первое число положительное, а второе отрицательное
  if a > 0 and b < 0:
    a, b = b, a
  # Создание списка квадратов
  sq = []
  for x in range(a, b + 1):
      sq.append(x**2)
  return sq

while True:
  # Ввод чисел пользователем
  a = input("Введите первое число: ")
  b = input("Введите второе число: ")
  # Проверка введенных значений
  try:
    a = float(a)
    b = float(b)
    break  # Если ввод корректный, выход из цикла 
  except ValueError:
    print("Некорректный ввод. Введите числа.")
# Получаем список квадратов
sq = sq_bet(a, b)

# Выводим список квадратов
print(f"Список квадратов чисел между {a} и {b}: ", sq)

