# 9. Даты
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
import datetime
# С клавиатуры вводится дата в формате DD-MM-YYYY. Нужно вывести дату начала недели,
# к которой относится введенная дата (дата понедельника недели), в таком же формате.

# Формат ввода
# 22-09-2022

# Формат вывода
# 19-09-2022

# Примечания
# Если введен понедельник - нужно вывести его же.

from datetime import datetime, timedelta


def get_start_week(date_input: datetime) -> datetime:
    date_input = date_input - timedelta(date_input.weekday())
    return date_input


def main() -> None:
    user_data = input().strip()
    pars_data = datetime.strptime(user_data, "%d-%m-%Y")
    start_week = get_start_week(pars_data)
    print(datetime.strftime(start_week, "%d-%m-%Y"))


if __name__ == '__main__':
    main()