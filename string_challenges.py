# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel_letters = 'аеёиоуыэюя'

answer = 0
for letter in word.lower():
    if letter in vowel_letters:
        answer += 1

print(answer)        


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
splitted_sentence = sentence.split()
sum_len = 0

for word in splitted_sentence:
    sum_len += len(word)

avg_len = sum_len / len(splitted_sentence)
print(round(avg_len))