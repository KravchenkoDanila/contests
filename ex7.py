<<<<<<< HEAD
# 7. Коллекции. Множества
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# С клавиатуры вводится строка, содержащая произвольное количество
# слов через запятую и пробел. Слова могут повторяться. Нужно вывести на
# экран все слова в алфавитном порядке по одному разу, также через пробел и запятую.

# Формат ввода
# джек, воробей, капитан, джек, воробей

# Формат вывода
# воробей, джек, капитан
#
# Примечания
# Обратите внимание, что в примере у первого слова "воробей" стоит запятая,
# а у второго - нет. В решении такие случае следует учесть. Кроме того, слова могут
# быть написаны в разном регистре. Вывести их нужно в нижнем регистре. Одинаковые слова,
# написанные в разных регистрах, считаем одинаковыми.


PUNCTUATION = {',', '.', '"', "'", ':', ';', '(', ')', '?', '!'}


def punctuation_clean(user_string: str, punc_set: set = PUNCTUATION) -> str:
    result_string = user_string.lower()
    for char in punc_set:
        if char in result_string:
            result_string = result_string.replace(char, " ")
    return result_string


def split_and_sort(user_string: str) -> list:
    words = user_string.split()
    unic_words = set(words)
    return sorted(unic_words)


def main() -> None:
    user_string = input()
    clean_string = punctuation_clean(user_string)
    sort_list = split_and_sort(clean_string)
    output_string = ", ".join(sort_list)
    print(output_string)


if __name__ == '__main__':
=======
# 7. Коллекции. Множества
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# С клавиатуры вводится строка, содержащая произвольное количество
# слов через запятую и пробел. Слова могут повторяться. Нужно вывести на
# экран все слова в алфавитном порядке по одному разу, также через пробел и запятую.

# Формат ввода
# джек, воробей, капитан, джек, воробей

# Формат вывода
# воробей, джек, капитан
#
# Примечания
# Обратите внимание, что в примере у первого слова "воробей" стоит запятая,
# а у второго - нет. В решении такие случае следует учесть. Кроме того, слова могут
# быть написаны в разном регистре. Вывести их нужно в нижнем регистре. Одинаковые слова,
# написанные в разных регистрах, считаем одинаковыми.


PUNCTUATION = {',', '.', '"', "'", ':', ';', '(', ')', '?', '!'}


def punctuation_clean(user_string: str, punc_set: set = PUNCTUATION) -> str:
    result_string = user_string.lower()
    for char in punc_set:
        if char in result_string:
            result_string = result_string.replace(char, " ")
    return result_string


def split_and_sort(user_string: str) -> list:
    words = user_string.split()
    unic_words = set(words)
    return sorted(unic_words)


def main() -> None:
    user_string = input()
    clean_string = punctuation_clean(user_string)
    sort_list = split_and_sort(clean_string)
    output_string = ", ".join(sort_list)
    print(output_string)


if __name__ == '__main__':
>>>>>>> b7439a16ff0a0a8a76c1ba6bcaf395cb8319a60e
    main()