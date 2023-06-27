def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")


class MyError(Exception):
    def _init_(self, text):
        self.txt = text


choice = input("Введите номер операции (1/2/3/4): ")
try:
    choice_check = int(choice)
    if choice_check > 4:
        raise MyError("Введен неверный номер операции")

    num1 = float(input("Введите первое число: "))
    # num1 = float(f"{input('Введите первое число: ')} \n ")
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Неверный ввод")

except MyError as mr:
    print(mr)
except ZeroDivisionError:
    print('ZeroDivisionError, You can not divide by zero')
except ArithmeticError:
    print('ArithmeticError')
except LookupError:
    print('LookupError')
except NameError:
    print('NameError, Input the numbers plz, it is not a messenger!!!')
except Exception:
    print('SomeError, Try to guess which one :)')
