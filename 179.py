posledov = input("введите последовательность чисел через пробел ", )
numba = int(input("введите любое число ", ))

def is_int(str):  # Определяем цифры в строке
    str = str.replace(" ", "")
    try:
        int(str)
        return True
    except ValueError:
        return False


if " " not in posledov:  # Проверка условия
    print("отсутствуют пробелы!")
    posledov = input("введите последовательность чисел через пробел ")
if not is_int(posledov):
    print("Введенная последовательность не цифры, либо не целые числа!")
    print("не соответствует заданному условию")
else:
    posledov = posledov.split()


list_posledov = [int(item) for item in posledov]


def merge_sort(L):  # сортировка
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_posledov = merge_sort(list_posledov)


def binary_search(array, element, left, right):  # Определение позиции
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return "Введенное число не входит в последовательность"


"""Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу."""


print(f'Упорядоченный по возрастанию список: {list_posledov}')

if not binary_search(list_posledov, numba, 0, len(list_posledov)):
    rI = min(list_posledov, key=lambda x: (abs(x - numba), x))
    ind = list_posledov.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < numba:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_posledov[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_posledov.index(rI)}
В списке нет меньшего элемента''')
    elif rI > numba:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_sequence_numbers.index(rI)}
Ближайший меньший элемент: {list_posledov[min_ind]} его индекс: {min_ind}''')
    elif list_posledov.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_sequence_numbers.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_posledov, numba, 0, len(list_posledov))}')

