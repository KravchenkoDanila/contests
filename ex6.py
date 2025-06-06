# 6. Коллекции. Списки
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# С клавиатуры подается 5 чисел, разделенных концом строки.
# Нужно вывести их на экран от большего к меньшему, также разделяя их концом строки.

# Формат ввода
# 12
# 1
# 45
# 9
# 10

# Формат вывода
# 45
# 12
# 10
# 9
# 1

def writing_in_list(iteration=5) -> list:
    result_list = []
    while iteration > 0:
        iteration -= 1
        num = input()
        if num == "":
            break
        try:
            result_list.append(int(num))
        except ValueError:
            break

    return result_list


def main():
    num_list = writing_in_list()
    num_list.sort(reverse=True)
    print("\n".join(map(str, num_list)))


if __name__ == '__main__':
    main()