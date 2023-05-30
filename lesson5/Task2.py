n = int(input('Введите натуральное число n: '))
def fact(n):
    if n <= 1:
        return 1
    return fact(n - 1) * n

print('Факториал n равен:',fact(n))
