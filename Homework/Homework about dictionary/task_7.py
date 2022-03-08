# Создайте словарь, связав его с переменной school,
# и наполните данными, которые бы отражали количество
# учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся,
# б) в школе появился новый класс,
# с) в школе был расформирован (удален) другой класс.
# Вычислите общее количество учащихся в школе
school = {
    '1a': 10, '1б': 15, '2б': 6, '6a': 12, '7в': 13,
    '8а': 18, '9б': 9, '10б': 16
}
school['6a'] = 900
school['11г'] = 40
del school['1a']
result = 0
for i in school.values():
    result += i
print(f' {school=} \n {result=}')
