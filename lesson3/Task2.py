user_name = input('Введите ваше имя: ')
user_age = input('Сколько вам лет? ')

if user_age.isdigit():
    user_age = int(user_age)

else:
    print('Ошибка повторите ввод')

if int(user_age) >= 0:
    user_age = int(user_age)

else:
    print('Ошибка повторите ввод')

if 0 < user_age < 10:
    print('Привет шкет', user_name)

if 10 < user_age < 18:
    print("Как жизнь?", user_name)

if 18 < user_age < 100:
    print("Что желаете господин?", user_name)
else:
    print(user_name, 'вы лжете в наше время столько не живут..')
