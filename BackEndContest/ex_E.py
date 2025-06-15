# E. Финикийские сообщения
# Ограничение времени	4 секунды
# Ограничение памяти	512 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Учёные нашли остатки сообщений от древней цивилизации финикийцев — создателей одного из первых алфавитов,
# который использовали для торгов, дипломатии, в религиозных текстах. Финикийцы были морской цивилизацией,
# активно торговавшей по всему Средиземноморью. Для передачи сообщений между кораблями или поселениями
# они использовали систему из девяти барабанов, где количество ударов по конкретному барабану определяло
# букву сообщения, — похожая система добралась до наших дней в кнопочных телефонах с режимом ввода Т9.

# Барабан	Буквы
# 1	- (не используется)
# 2	ABC
# 3	DEF
# 4	GHI
# 5	JKL
# 6	MNO
# 7	PQRS
# 8	TUV
# 9	WXYZ

# Например, чтобы набрать U, финикийцы дважды ударяли по барабану номер 8, а чтобы набрать Z,
# они четырежды били по барабану с номером 9. Сообщение HELLOWORLD от них выглядит так: 443355555566696667775553.

# Известно, что финикийцы используют только слова из словаря. Словом является последовательность
# буквенных символов без пробелов и иных знаков. Сообщение, которое нашли учёные, как раз связано
# с ритмами барабанов. Ваша задача — при помощи словаря расшифровать сообщение, переданное финикийцами.

# Пример 1
# Ввод
# 443355555566696667775553
# 3
# WORLD
# QUANTUM
# HELLO

# Вывод
# HELLO WORLD

# Пример 2
# Ввод
# 7788266888674499977774442227777
# 5
# PHYSICS
# QUANTUM
# WORLD
# HELLO
# PHYS

# Вывод
# QUANTUM PHYSICS

def build_letter_to_code():
    return {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'
    }


def load_dictionary(n, letter_to_code):
    dictionary = []
    for _ in range(n):
        word = input().strip()
        code = ''.join(letter_to_code[c] for c in word)
        dictionary.append((code, word))
    return dictionary


def decode_message(s, dictionary):
    length = len(s)
    dp = [False] * (length + 1)
    prev = [-1] * (length + 1)
    word_at = {}

    dp[0] = True

    for i in range(length):
        if dp[i]:
            for code, word in dictionary:
                if s.startswith(code, i):
                    j = i + len(code)
                    if not dp[j]:
                        dp[j] = True
                        prev[j] = i
                        word_at[j] = word

    result = []
    pos = length
    while pos > 0:
        result.append(word_at[pos])
        pos = prev[pos]

    return ' '.join(reversed(result))


def main():
    s = input().strip()
    n = int(input().strip())
    letter_to_code = build_letter_to_code()
    dictionary = load_dictionary(n, letter_to_code)
    decoded = decode_message(s, dictionary)
    print(decoded)


if __name__ == "__main__":
    main()