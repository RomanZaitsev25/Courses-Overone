# Есть список состоящий из слов и чисел, нужно записать
# в файл сначала слова в порядке возрастания
# их длинны, а после слов цифры в порядке возрастания

a = ['roman', 'mother', 'dad', 1, 2, 9, 5]
print('List:', a)
list_of_words = []
list_of_numbers = []
f = open('file_4.txt', 'a')
for i in a:
    if type(i) is str:
        list_of_words.append(i)
    elif type(i) is int:
        list_of_numbers.append(i)
list_of_words.sort()
list_of_numbers.sort()
print(list_of_words)
print(list_of_numbers)

for i in list_of_words:
    f.write(i + '\n')
for i in list_of_numbers:
    i = str(i)
    f.write(i + '\n')
f.close()