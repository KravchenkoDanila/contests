# 2. Ближайшее число
# Напишите программу, которая находит в массиве элемент,
# самый близкий по величине к данному числу.

# Формат ввода
# В первой строке задается одно натуральное число N,
# не превосходящее 1000 — размер массива. Во второй строке содержатся N чисел — элементы массива,
# целые числа, не превосходящие по модулю 1000. В третьей строке вводится одно целое число x,
# не превосходящее по модулю 1000.

# Формат вывода
# Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них.


def binary_search(arr: list, target: int) -> int:
    l = 0
    r = len(arr) - 1

    if target <= arr[l]:
        return arr[l]
    if target >= arr[r]:
        return arr[r]

    while l < r:
        m = (l + r) // 2
        if arr[m] == target:
            return arr[m]
        elif arr[m] < target:
            l = m + 1
        else:
            r = m

    if arr[r] - target >= target - arr[r-1]:
        return arr[r - 1]
    else:
        return arr[r]


def array_init() -> list:
    n = int(input())
    arr = list(map(int, input().split()))
    if n == len(arr):
        arr.sort()
        return arr


def main() -> None:
    arr = array_init()
    target = int(input())
    result = binary_search(arr, target)

    print(result)


if __name__ == '__main__':
    main()