# Один кортеж вводится с клавиатуры (допустимы только численные значения).
# Вывести индекс(ы) элементов имеющих максимальное значение.

# 1 Вариант решения
import ast
t1 = ast.literal_eval(input('Enter the numbers:'))
max_values = max(t1)
print('Max_value_with_index:', t1.index(max_values))

# 2 Вариант решения
import ast
t1 = ast.literal_eval(input('Enter the numbers:'))
for symbol, j in enumerate(t1):
    if j == max(t1):
        print('Index: {}'.format(symbol))

