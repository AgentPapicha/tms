user_lst = input('Введите элементы для списка через пробел:').split()
lst = [1, 2, 3, 4, 2, 3, 2, 2]


def analysis(from_list, to_dict):
    for i in from_list:
        if i in to_dict:
            to_dict[i] += 1
        else:
            to_dict[i] = 1


dct = {}
analysis(user_lst, dct)

for item in sorted(dct):
    print(f"Число {item} Повторяется раз - {dct[item]}")
