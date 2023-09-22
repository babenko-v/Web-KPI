import copy
print("Алгоритм пошуку Фібоначчі потребують сортування файлу за алфавітною послідовністю, дані з початкового файлу будуть"
      "відсортовані і записані у новий текстовий файл")


def repit():
    global meter
    meter += 1
    index = fibonacci_search(sorted_list, word)
    if index == -1:
        print("Слово '{}' не знайдено в текстовому файлі.".format(word))
    else:
        print("Слово '{}' найдено в текстовому файлі на {} рядку.".format(word, lines.index(word) + meter))
        sorted_list.pop(index)
        lines.pop(lines.index(word))
    if meter >= count:
        return
    else:
        repit()

def repit_2():
    global meter
    meter += 1
    index = fibonacci_search(sorted_list, word_copy)
    if index == -1:
        print("Слово '{}' не знайдено в текстовому файлі.".format(word))
    else:
        print("Слово '{}' знайдено в текстовому файлі на {} рядку.".format(word, lines.index(word_copy) + meter))
        sorted_list.pop(index)
        lines.pop(lines.index(word_copy))
    if meter >= count:
        return
    else:
        repit_2()

def fibonacci_search(arr, x):
    # Инициализация переменных чисел Фибоначчи
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    fib_n = fib_n_minus_1 + fib_n_minus_2

    # Находим ближайшее число Фибоначчи, которое больше или равно длине массива
    while fib_n < len(arr):
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
        fib_n = fib_n_minus_1 + fib_n_minus_2

    # Индекс, с которого начинается текущий поиск
    index = -1

    # Пока есть числа Фибоначчи для проверки
    while fib_n > 1:
        # Вычисляем индекс следующего элемента
        i = min(index + fib_n_minus_2, len(arr) - 1)

        # Если элемент меньше искомого значения, сдвигаем индекс и числа Фибоначчи на два шага назад
        if arr[i] < x:
            fib_n = fib_n_minus_1
            fib_n_minus_1 = fib_n_minus_2
            fib_n_minus_2 = fib_n - fib_n_minus_1
            index = i
        # Если элемент больше искомого значения, сдвигаем индекс и числа Фибоначчи на один шаг назад
        elif arr[i] > x:
            fib_n = fib_n_minus_2
            fib_n_minus_1 = fib_n_minus_1 - fib_n_minus_2
            fib_n_minus_2 = fib_n - fib_n_minus_1
        # Иначе элемент найден
        else:
            return i

    # Если элемент не найден, возвращаем -1
    if fib_n_minus_1 and index < len(arr) - 1 and arr[index + 1] == x:
        return index + 1
    else:
        return -1

with open('zadanie.txt', 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]
sorted_list = sorted(lines)

with open('sort.txt', 'w') as file:
    for line in sorted_list:
        file.write(line + '\n')
choose = int(input('Як ви хочете вести послідовності символів 1 - як окреме слово, 2 - як послідовність символів:\n'))
question = input("В якому форматі хочете знайти слово, з врахуванням регістру символів(yes - no)?\n")
check = True
if choose == 1:
    word = str(input("Введіть слово, яке ви хочете знайти у файлі: "))
    word_copy = copy.copy(word)
    if question == 'yes':
        count, meter = lines.count(word), 0
        repit()
    elif question == 'no':
        word_copy = word_copy.lower()
        sorted_list = [item.lower() for item in sorted_list]
        sorted_list = sorted(sorted_list)
        lines = [item.lower() for item in lines]
        count, meter = sorted_list.count(word_copy), 0
        repit_2()
elif choose == 2:
    symbols = str(input("Введіть послідовність символів, яку ви хочете знайти у файлі:\n"))
    symbols_copy = copy.copy(symbols)
    if question == 'yes':
        meter = 0
        for item in lines:
            if symbols in item:
                meter += 1
                print(f"Послідовність символів {symbols} є частиної імені {item}, яка знаходиться на {lines.index(item)+meter} рядку,"
                      f"beg {item.index(symbols)}, end {len(symbols)+len(item[:item.index(symbols)])-1}")
                lines.pop(lines.index(item))
                check = False
        if check:
            print("Послідовність символів '{}' не знайдено в текстовому файлі.".format(symbols))
    elif question == 'no':
        lines = [item.lower() for item in lines]
        symbols_copy = symbols_copy.lower()
        meter = 0
        for item in lines:
            if symbols_copy in item:
                print(f"Послідовність символів {symbols} є частиної імені {item}, яка знаходиться на {lines.index(item)+meter+1} рядку, "
                      f"beg {item.index(symbols_copy)}, end {len(symbols)+len(item[:item.index(symbols_copy)])-1}")
                lines.pop(lines.index(item))
                check = False
                meter += 1
        if check:
            print("Послідовність символів '{}' не знайдено в текстовому файлі.".format(symbols))

