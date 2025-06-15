# 1. Словарь синонимов
# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для одного данного слова определите его синоним.

# Формат ввода
# Программа получает на вход количество пар синонимов N.
# Далее следует N строк, каждая строка содержит ровно два слова-синонима.
# После этого следует одно слово.

# Формат вывода
# Программа должна вывести синоним к данному слову.

# Примечание
# Эту задачу можно решить и без словарей (сохранив все входные данные в списке), но решение со словарем будет более простым.


#TODO переименовать переменные и функции нормально


def intional_dict() -> dict:
    sinonims = {}
    try:
        n = int(input())
        for i in range(n):
            word1, word2 = map(str, input().split())
            sinonims[word1] = word2
        return sinonims
    except:
        print("введено неверное значение")


def sinonim_search(word: str, worder: dict) -> str:
    try:
        return worder[word]
    except KeyError:
        for k, v in worder.items():
            if v == word:
                return k
    return ''


def main() -> None:
    sinonims = intional_dict()
    word = input()
    result = sinonim_search(word, sinonims)
    print(result)


if __name__ == '__main__':
    main()