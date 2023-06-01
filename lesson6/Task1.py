def recursive_simple(src: dict, lookup_value: str | list, level=1):
    for key, current_value in src.items():
        if isinstance(current_value, dict):
            return recursive_simple(current_value, lookup_value, level+1)
            # функция вызывает сама себя, используя в качестве аргумента
            # 'src' переменную v, которая имеет тип dict
        else:
            if current_value == lookup_value:
                return f"Значение {current_value} найдено на глубине: {level}"


# source_dict = {
#     'key1': 'John',
#     'key2': {
#         'key3': 'Bob',
#         'key4': {
#             'key5': 'Alex',
#             'key6': {
#                 'key7': {
#                     'key8': 'Robert'
#                 }
#             },
#         },
#     }
# }

src2 = {
        'key2': {
            'key3': 'Ann',  # deep 1
            'key4': {
                'key5': ['Kate', 'Mary'],  # deep 2
                'key6': {
                    'key7': [
                        'Bob',  # deep 3
                        'Duke',
                        {
                            'key8': {  # deep 4
                                'key9': [  # deep 5
                                    'Lisa',
                                    {
                                        'key10': ['Mark', 'Alex']  # deep 6
                                    }
                                ],
                                "key11": "Louisa",  # deep 5
                            }
                        },
                        "Alex",  # deep 3
                    ]
                },
            },
            'key12': 'Robert'  # deep 1
        },
        "key13": "Ronaldo"  # d
}

# print(recursive_simple(source_dict, 'Alex'))  # напечатает 'Alex is found!'
# print(recursive_simple(source_dict, 'Bob'))   # напечатает 'Alex is found!'
# print(recursive_simple(source_dict, 'Jessica'))

print(recursive_simple(src2, 'Kate'))  # напечатает 'Alex is found!'
print(recursive_simple(src2, 'Robert'))   # напечатает 'Alex is found!'
print(recursive_simple(src2, 'Ronaldo'))
