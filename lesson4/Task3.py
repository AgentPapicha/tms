my_list = list(range(1, 101))
result = [(x if x % 10 == 0 else x * 10 if x % 4 != 0 else x * 2) for x in my_list]
print(result)
