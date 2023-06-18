random_string = input('Input a random number string: ')

even_numbers = random_string[::2]
odd_numbers = random_string[1::2]

print('The input string:', random_string)
print(even_numbers, odd_numbers)
print('The even numbers of a string:', even_numbers)
print('The odd numbers of a string:', odd_numbers)
