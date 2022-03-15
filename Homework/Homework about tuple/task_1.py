# Два кортежа вводятся с клавиатуры (допустимы только численные значения).
# Вывести тот кортеж, произведение элементов которого больше
import ast

t1 = ast.literal_eval(input('Enter the numbers:'))
t2 = ast.literal_eval(input('Enter the numbers:'))
composition_1 = 1
composition_2 = 1
for i in t1:
    composition_1 += i
for i in t2:
    composition_2 += i
if composition_1 > composition_2:
    print('Tuple_1:', t1)
else:
    print('Tuple_2:', t2)
