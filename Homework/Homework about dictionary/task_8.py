# У нас есть словарь, где ключ название продукта.
# Значение, список, который содержит цену и количество товара.
# вывести через '-' название цену количества.

product = {'Apple': ['12euro', '12штук']}

for key, value in product.items():
    print(key, '-', value)