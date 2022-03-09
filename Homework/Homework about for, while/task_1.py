# В строке посчитать количество глассных букв
text = input('Enter the new text:').lower()
letters = 'euioaуеыаоэяию'
s = 0
for i in text:
    if i in letters:
        s += 1
print(s)

