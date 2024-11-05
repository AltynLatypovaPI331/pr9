import random
# Меняет местами минимальный и максимальный элементы в списке чисел.
def min_max(ns):
  # Проверка на наличие элементов
  if len(ns) == 0:
    print("Нет элементов в списке.")
    return ns
  # Проверка на колличество элементов
  if len(ns) == 1:
    print("В списке только один элемент.")
    return ns
  # Проверка на одинаковые элементы
  if all(x == ns[0] for x in ns):
    print("Все элементы в списке одинаковые.")
    return ns
  # Проверка на нечисловые или булевые значения
  for n in ns:
    try:
      # Преобразование к float
      float(n) 
    except ValueError:
      print("В списке есть нечисловое или булевое значение.")
      return ns
  # Поиск минимального и максимального элементов
  min_index = ns.index(min(ns))
  max_index = ns.index(max(ns))

  # Обмен местами минимального и максимального элементов
  ns[min_index], ns[max_index] = ns[max_index], ns[min_index]

  return ns
random_ns = [random.randint(1, 100) for _ in range(10)]
print(f"Рандомный список: {random_ns}")

# Обмен минимального и максимального элементов
s_ns = min_max(random_ns)
print(f"Список после обмена: {s_ns}")

# Примеры использования
ns1 = [1, 2, 3, 4, 5]
print(f"Исходный список: {ns1}")
print(f"Список после обмена: {min_max(ns1)}")

ns2 = [-4.5, -4.5, -4.5, -4.5, -4.5]
print(f"Исходный список: {ns2}")
print(f"Список после обмена: {min_max(ns2)}")

ns3 = [1]
print(f"Исходный список: {ns3}")
print(f"Список после обмена: {min_max(ns3)}")

ns4 = []
print(f"Исходный список: {ns4}")
print(f"Список после обмена: {min_max(ns4)}")

ns5 = [1, 2, 'a', 4, 5]
print(f"Исходный список: {ns5}")
print(f"Список после обмена: {min_max(ns5)}")

ns6 = [1, 2, True, 4, 5]
print(f"Исходный список: {ns6}")
print(f"Список после обмена: {min_max(ns6)}")