from string import Template
user_sentence = input("Введите предложение из двух слов: ")
words = user_sentence.split()

first_word = words[0]
second_word = words[1]

word1 = words[0]
word2 = words[1]

print("!" + second_word + " ! " + first_word + "!")

s = Template('!$word2 ! $word1!')

print(s.substitute(word1=word1, word2=word2))