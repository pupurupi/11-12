# Вариант 14. Реализуйте решение судоку с помощью backtracking
# Функция красивого вывода судоку с полем
def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("— " * 11)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def find_empty(board):
    # Находит следующую пустую клетку (0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None
def is_valid(board, num, pos):
    # Проверяет, можно ли поставить число num в позицию pos
    row, col = pos
    # Проверка строки
    for j in range(9):
        if board[row][j] == num and j != col:
            return False
    # Проверка столбца
    for i in range(9):
        if board[i][col] == num and i != row:
            return False
    # Проверка квадрата 3x3
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True
def solve_sudoku(board):
    # Решает судоку с помощью backtracking
    empty = find_empty(board)
    # Базовый случай (если нет пустых клеток, то судоку решено)
    if not empty:
        return True
    row, col = empty
    # Пробуем числа от 1 до 9
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            # Пробуем поставить число
            board[row][col] = num
            # Рекурсивная чаить: рекурсивно решаем оставшуюся часть
            if solve_sudoku(board):
                return True
            # Backtrack: если не привело к решению
            board[row][col] = 0
    # Не нашли подходящего числа
    return False
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
print("Исходное судоку:")
print_sudoku(sudoku_board)
print()
    
if solve_sudoku(sudoku_board):
    print("Решенное судоку:")
    print_sudoku(sudoku_board)
else:
    print("Решение не найдено!")