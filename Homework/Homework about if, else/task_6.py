# Создать обменный пункт валюты. Деньги вводятся через клавиатуру, динамически.
# В банкомате три типа валют(доллары, евро, рубли).

usd = 2.6
euro = 4
rub100 = 2.8
money = int(input('Введите сумму, которую хотите поменять:'))
currency = int(input('Укажите код валюты (доллары - 1, евро - 2, рубли - 3):'))

if currency == 1:
    cash = round(money / usd, 2)
    print('Валюта:, доллары США')

if currency == 2:
    cash = round(money / euro, 2)
    print('Валюта:, евро')

if currency == 3:
    cash = round(money / rub100, 3)
    print('Валюта:, российские рубли')

print('Получено денег:', cash)
