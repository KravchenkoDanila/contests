# 8. Коллекции. Словари
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# С клавиатуры вводятся слова через запятую с пробелом. Выведите на экран три наиболее часто встречаемых слова,
# вместе с количеством этих слов. Количество должно быть отделено от слова двоеточием и пробелом.
# Каждая пара слово-количество должна быть выведена на отдельной строчке. Для простоты гарантируется,
# что в строке нет слов с одинаковой встречаемостью.

# Формат ввода
# три, три, и, ещё, три, будет, дырка, и, будет, и, дырка, и, дырка, и, дырка

# Формат вывода
# и: 5
# дырка: 4
# три: 3

# Примечания
# Рекомендация: чтобы быстрее решить задачу, нужно составить словарь, в котором ключами будут встреченные слова,
# а значениями - их количество в строке. Далее работайте с этим словарем по своему усмотрению.
# Далее один из вариантов - отсортировать кортежи, в которых на первом месте стоит количество слов,
# а на втором - сами слова.

# Учтите, что различных слов в строке может быть меньше трех. В этом случае нужно вывести все.


PUNCTUATION = {',', '.', '"', "'", ':', ';', '(', ')', '?', '!'}


def punctuation_clean(user_string: str, punc_set: set = PUNCTUATION) -> str:
    result_string = user_string.lower()
    for char in punc_set:
        if char in result_string:
            result_string = result_string.replace(char, " ")
    return result_string


def make_top_words_dict(user_string: str) -> list[tuple]:
    clean_string = punctuation_clean(user_string)
    item_list = clean_string.split()
    counter_dict = {}
    for item in item_list:
        counter_dict[item] = counter_dict.get(item, 0) + 1
    top_list = sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)
    return top_list


def top_n_output(top_list: list[tuple], n: int = 3) -> None:
    limit = min(n, len(top_list))
    for i in range(limit):
        print(f"{top_list[i][0]}: {top_list[i][1]}")


def main() -> None:
    user_input = input()
    top_list = make_top_words_dict(user_input)
    top_n_output(top_list)


if __name__ == '__main__':
    main()