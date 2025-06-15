
populars_lang = {}

student = int(input())
for i in range(student):
                                            #TODO рефакторинг (разбиение по фенкциям, переименование переменных)
    lang_num = int(input())

    for i in range(lang_num):

        langue = input()
        if langue != '':

            populars_lang[langue] = populars_lang.get(langue, 0) + 1

all_list = populars_lang.keys()
popular_list = []

for key, value in populars_lang.items():
    if value == student:
        popular_list.append(key)

print(len(popular_list))
for i in popular_list:
    print(i)

print(len(all_list))
for i in all_list:
    print(i)


