user_sentence = input("Введите предложение из двух слов: ")
words = user_sentence.split()

words[0], words[1] = words[1], words[0]
new_sentence = " ! ".join(words)
new_sentence = "!" + new_sentence + "!"

print(new_sentence)