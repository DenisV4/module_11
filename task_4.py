print('Задача 4. Первая цифра\n')

# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками

# Пример:
# Введите число: 123.456
# Первая цифра после десятичной точки: 4

print(f"Первая цифра после десятичной точки: {int(float(input("Введи число: ")) * 10) % 10}")
