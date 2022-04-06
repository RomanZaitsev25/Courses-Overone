# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так,
# чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длины

f = open('file_1.txt', 'r')
lines = f.readlines()
print('Lines=', lines)
list_of_numbers = []
list_of_words = []
for line in lines:
    numbers_or_words = line.replace('\n', '')
    if numbers_or_words.isdigit():
        list_of_numbers.append(int(numbers_or_words))
    else:
        list_of_words.append(numbers_or_words)
list_of_numbers = sorted(list_of_numbers)
print('List_of_numbers=', list_of_numbers)
list_of_words = sorted(list_of_words, key=len)
print('List_of_words=', list_of_words)
result_list = []
result_list.extend(list_of_numbers)
result_list.extend(list_of_words)
print('Result_list:', result_list)
f.close()


# list_of_numbers = []
# list_of_words = []
# for line in lines:
#     numbers_or_words = line.replace('\n', '')
#     if numbers_or_words.isdigit():
#         list_of_numbers.append(int(numbers_or_words))
#         print('list_of_numbers', list_of_numbers)
#     else:
#         list_of_words.append(numbers_or_words)
#         print('list_of_words', list_of_words)
# list_of_numbers = sorted(list_of_numbers)
# print(list_of_numbers)
# list_of_words = sorted(list_of_words, key=len)
# print(list_of_words)
# result_list = []
# result_list.extend(list_of_numbers)
# result_list.extend(list_of_words)
# print(result_list)
# f.close()