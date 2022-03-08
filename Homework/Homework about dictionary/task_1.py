# Методы определния словаря
d = {'roman': 2}
d1 = dict(roman=2)
d3 = dict([('roman', 2)])
d4 = dict.fromkeys(['roman'], 2)
d5 = {'roman': 2 ** 1 for i in range(1)}
print(d)
print(d1)
print(d3)
print(d4)
print(d5)
