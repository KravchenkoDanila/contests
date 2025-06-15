# 15. Парсинг JSON
# Ограничение времени	10 секунд
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt

# Задачи, аналогичные этой, часто встречаются в реальной веб-разработке. Будем получать и отдавать JSONы.
# К вам поступают данные в виде json-строки, в которых содержится список людей.
# Для каждого человека описаны различные его параметры, но вам нужно посчитать просто средний возраст всех людей из списка.
# Напишите функцию mean_age(json_string), которая принимает json строку, считает средний возраст людей из входных данных
# и возвращает новую json-строку в том формате, который указан ниже.

# Формат ввода
# [
#     {
#         "name": "Петр",
#         "surname": "Петров",
#         "patronymic": "Васильевич",
#         "age": 23,
#         "occupation": "ойтишнек"
#     },
#     {
#         "name": "Василий",
#         "surname": "Васильев",
#         "patronymic": "Петрович",
#         "age": 24,
#         "occupation": "дворник"
#     }
# ]

# Формат вывода
# {"mean_age": 23.5}

import json


def mean_age(json_string: str) -> str:

    try:
        data = json.loads(json_string)
    except json.JSONDecodeError:
        return json.dumps({"mean_age": 0})

    user_cntr = 0
    total_age = 0

    for user in data:
        if user["age"] is not None:
            total_age += user["age"]
            user_cntr += 1
    return json.dumps({"mean_age": total_age / user_cntr})


def main() -> None:
    j = '''[
        {
            "name": "Петр",
            "surname": "Петров",
            "patronymic": "Васильевич",
            "age": "",
            "occupation": "ойтишнек"
        },
        {
            "name": "Василий",
            "surname": "Васильев",
            "patronymic": "Петрович",
            "age": "",
            "occupation": "дворник"
        }
    ]'''
    print(mean_age(j))


if __name__ == '__main__':
    main()