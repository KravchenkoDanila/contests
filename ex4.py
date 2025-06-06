# 4. Строки. Поиск подстрок
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# С клавиатуры вводится строка, а затем - подстрока.
# В строке найти все слова, в которых содержится заданная подстрока,
# и вывести эти слова целиком. Если слова повторяются, вывести все повторения.
#
# Формат ввода

# Раз два три четыре пять
# а
#
# Формат вывода

# Раз
# два

# Примечания
# Регистр слов не должен учитываться. Но вывод слов должен производиться
# в том же виде, в котором они были поданы в первоначальной строке.

def find_words_containing_substring(user_string: str, substring: str) -> list:
    user_words = user_string.split()
    result_list = []
    for word in user_words:
        if substring.lower() in word.lower():
            result_list.append(word)
    return result_list


def main():
    user_string = input()
    searching_substring = input()
    output_list = "\n".join(find_words_containing_substring(user_string, searching_substring))
    print(output_list)


if __name__ == '__main__':
    main()