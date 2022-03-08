s# Класс Human
# Создайте класс Human.
# Определите для него два статических поля: default_name и default_age.
# Создайте метод __init__(), который помимо self
# принимает еще два параметра: name и age.
# Для этих параметров задайте значения по умолчанию,
# используя свойства default_name и default_age.
# В методе __init__() определите четыре свойства:
# Публичные - name и age. Приватные - money и house.
# Реализуйте справочный метод info(),
# который будет выводить поля name, age, house и money.
# Реализуйте справочный статический метод default_info(),
# который будет выводить статические поля default_name и default_age.
# Реализуйте метод earn_money(), увеличивающий значение свойства money.
#                            Тесты
# Вызовите справочный метод default_info() для класса Human()
# Создайте объект класса Human
# Выведите справочную информацию о созданном объекте (вызовите метод info()).
# Поправьте финансовое положение объекта - вызовите метод earn_money()
# Посмотрите, как изменилось состояние объекта класса Human №#
# Класс House
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него
# два динамических свойства: _area и _price.
# 3. Свои начальные значения они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра
# размер скидкии возвращает цену с учетом данной скидки.
#
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так,
# чтобы он создавал объект с площадью 40м2
#
# Класс Human
# Реализуйте приватный метод make_deal(), который будет отвечать за
# техническую реализацию покупки дома: уменьшать количество денег
# на счету и присваивать ссылку на только что купленный дом.
# В качестве аргументов данный метод принимает объект дома и его цену.
# Реализуйте метод buy_house(), который будет проверять,
# что у человека достаточно денег для покупки, и совершать сделку.
# Если денег слишком мало - нужно вывести предупреждение в консоль.
# Параметры метода: ссылка на дом и размер скидки
#                Тесты
# Создайте объект класса SmallHouse
# Попробуйте купить созданный дом, убедитесь в получении предупреждения.
# Снова попробуйте купить дом, после поправки финансового положения

class Human:
    default_name = 'Roman'
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__house = 'пр-т Мира,16'
        self.__money = 0

    def info(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'House:{self.__house}')
        print(f'Money:{self.__money}')

    @staticmethod
    def default_info():
        print(f'Default_name:{Human.default_name}')
        print(f'Default_age:{Human.default_age}')

    def earn_money(self, money):
        self.__money += money

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money < price:
            print('Мало денег')
        else:
            self.__make_deal(house, price)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discaunt):
        return self._price * (1 - discaunt / 100)


class SmallHouse(House):

    def __init__(self, price):
        super().__init__('40м2', price)


if __name__ == '__main__':
    Human.default_info()
    human_obj = Human()
    human_obj.info()
    human_obj.earn_money(10000)
    human_obj.info()
    small_house_obj = SmallHouse(51000)
    human_obj.buy_house(small_house_obj, 15)
    human_obj.earn_money(50000)
    human_obj.buy_house(small_house_obj, 10)
    human_obj.info()
