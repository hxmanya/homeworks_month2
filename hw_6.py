def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array, value):
    pos = 0
    n = len(array)
    result_ok = False
    first = 0
    last = n - 1
    while first < last:
        middle = (first + last) // 2
        if value == array[middle]:
            first = middle
            last = first
            result_ok = True
            pos = middle
        else:
            if value > array[middle]:
                first = middle + 1
            else:
                last = middle - 1
    if result_ok:
        print("Элемент найден!")
        return pos
    else:
        print("Элемент не найден!")


if __name__ == '__main__':
    list_1 = [123, 3, 84, 912, 333, 85, 905, 10, 57, 724]
    print(f'Неотсортированный список: {list_1}')
    bubble_sort(list_1)
    print(f'Отсортированный список: {list_1}')
    index = binary_search(list_1, 123)
    print(f'Элемент {list_1[index]} в списке имеет индекс {index}!')
