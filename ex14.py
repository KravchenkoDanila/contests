# 14. Файлы
# Ограничение времени	10 секунд
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Напишите функцию get_popular_name_from_file(filename), которая считывает файл,
# в котором в каждой строке записаны имя и фамилия через пробел. filename - это имя файла,
# в котором записаны эти имена. Вам нужно вернуть строку - самое популярное имя в файле.
# Если таких имен несколько, они должны быть перечислены через запятую внутри строки в алфавитном порядке.


def dict_counter(word_list: list) -> dict:
    result_dict = {}

    for name in word_list:
        result_dict[name] = result_dict.get(name, 0) + 1
    return result_dict


def get_popular_name_from_file(filename):
    #===========Получение топа имен===========
    with open(filename, encoding='utf-8') as f:
        names_list = []
        for line in f:
            names_list.append(line.split()[0])

    top_names = sorted(dict_counter(names_list).items(), reverse=True, key=lambda x: x[1])

    #======Получение списка имен длч вывода======
    output_list = []
    for i in range(len(top_names)):
        if i == 0:
            output_list.append(top_names[0][0])
        else:
            if top_names[i][1] == top_names[i-1][1]:
                output_list.append(top_names[i][0])
            else:
                break
    output_list.sort()

    return (", ".join(output_list))


def main():
    file = "txt1.txt"
    print(get_popular_name_from_file(file))


if __name__ == '__main__':
    main()