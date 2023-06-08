first_string = input('Enter a first string: ')
second_string = input('Enter a second string: ')
third_string = input('Enter a third string: ')
fourth_string = input('Enter a fourth string: ')

file = open('user_strings.txt', 'w')
file.write(f"{first_string}\n{second_string}\n")
file.close()

file = open('user_strings.txt', 'a')
file.write(f"{third_string}\n{fourth_string}")
file.close()
