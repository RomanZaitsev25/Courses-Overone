# Развернть строку без использования среза
text = input('Enter the word:')
for i in reversed(text):
    print(i, end='')
