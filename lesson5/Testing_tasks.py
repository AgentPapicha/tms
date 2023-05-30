#Task1

# print (new_dic,type(new_dic))
# dic2 = reversed(dic)
# a = [['moskva', 495], ['piter', 812], ['penza', 8412]]
# dict.__reversed__(a)
# q = dict.fromkeys(['a', 'b', 'c'], 100)
# q2 = reversed(q)

#Task2
# def rec(x):
#     if x<4:
#         print(x)
#         rec(x+1)
#         print(x)
# rec(1)

#Task 3

from random import randint

# fill_list = [1, 2, 3, 4, 5, 6, 1, 7]
# def fill_list(minimum, maximum, amount, empty_list):
# #     for i in range(amount):
# #         empty_list.append(randint(minimum, maximum))
#
#
# def analysis(from_list, to_dict):
#     for i in from_list:
#         if i in to_dict:
#             to_dict[i] += 1
#         else:
#             to_dict[i] = 1
#
#
# lst = [1, 2, 3, 4, 2, 3]
# dct = {}
#
# #mn = int(input('Минимум: '))
# #mx = int(input('Максимум: '))
# # qty = int(input('Количество элементов: '))
#
# # fill_list(mn, mx, qty, lst)
# analysis(lst, dct)
#
# for item in sorted(dct):
#     # print(f"'{'Число'}': {'Повторяется раз'}")
#     print(f"'{'Число',item}': {'Повторяется раз', dct[item]}")
#     # print(f"'{item}': {dct[item]}")