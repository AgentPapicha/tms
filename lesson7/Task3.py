words = ('level', 'hello', 'racecar', 'python', 'madam', 'refer', 'minim', 'rotor', 'tenet', 'cookies')


# определяем функцию, которая проверяет, является ли слово полиндромом
def is_palindrome(word):
    return word == word[::-1]


# используем функцию filter() для отбора полиндромов из кортежа слов
palindromes = tuple(filter(is_palindrome, words))

print(palindromes)

"""
В данном примере мы определяем функцию `is_palindrome()`, которая принимает слово и возвращает `True`, 
если оно является полиндромом, и `False` в противном случае. Затем мы используем функцию `filter()` 
для отбора только тех слов из кортежа `words`, которые являются полиндромами. 
Результат сохраняем в новый кортеж `palindromes`. Наконец, выводим этот кортеж на экран.
"""
