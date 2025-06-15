# 4. Наибольшее произведение двух чисел
# Дан список, заполненный произвольными целыми числами.
# Найдите в этом списке два числа, произведение которых максимально.

# Формат ввода
# В единственной строке через пробел вводятся целые числа — элементы списка.
# Список содержит не менее двух и не более 100 000 чисел.
# Сами элементы по модулю не превышают 1 000 000.

# Формат вывода
# Выведите эти два числа в порядке неубывания.

# Примечание
# Решение должно иметь сложность O(n), где n — размер списка.

# Гарантируется, что во всех тестах ответ однозначен.

# Ограничение времени 1 с
# Ограничение памяти 64 МБ

def find_max_abs_pair(nums: list) -> list:
    if nums[0] > nums[1]:
        max1, max2 = nums[0], nums[1]
        min1, min2 = nums[1], nums[0]
    else:
        max1, max2 = nums[1], nums[0]
        min1, min2 = nums[0], nums[1]

    for i in range(2, len(nums)):
        if nums[i] > max1:
            max1, max2 = nums[i], max1
        elif nums[i] > max2:
            max2 = nums[i]

        if nums[i] < min1:
            min1, min2 = nums[i], min1
        elif nums[i] < min2:
            min2 = nums[i]

    if min1 * min2 < max1 * max2:
        return [max2, max1]

    else:
        return [min1, min2]

def main() -> None:
    nums = list(map(int, input().split()))
    num1, num2 = find_max_abs_pair(nums)
    print(num1, num2)


if __name__ == '__main__':
    main()