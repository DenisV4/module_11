print('Задача 6. Ход конём\n')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

while True:
    print("Введите местоположение коня: ")
    knight_x, knight_y = int(float(input()) * 10), int(float(input()) * 10)
    print("Введите местоположение точки на доске: ")
    target_x, target_y = int(float(input()) * 10), int(float(input()) * 10)

    if knight_x in range(8) and knight_y in range(8) and target_x in range(8) and target_y in range(8):
        break

    print("Неверные координаты. Попробуйте ещё раз.\n")

print(f"Конь в клетке ({knight_x}, {knight_y}). Точка в клетке ({target_x}, {target_y}).")

dx, dy = abs(knight_x - target_x), abs(knight_y - target_y)
is_valid_move = dx == 1 and dy == 2 or dx == 2 and dy == 1
message = "Да, конь может ходить в эту точку." if is_valid_move else "Нет, конь не может ходить в эту точку."

print(message)
