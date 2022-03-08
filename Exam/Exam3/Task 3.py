# Класс Tomato:
# 1. Создайте класс Tomato +
# 2. Создайте статическое свойство states, которое будет содержать
# все стадии созревания помидора +
# 3. Создайте метод __init__(), внутри которого будут определены
# два динамических protected свойства: 1) _index - передается параметром и
# 2) _state - принимает первое значение из словаря states +
# 4. Создайте метод grow(), который будет переводить томат
# на следующую стадию созревания +
# 5. Создайте метод is_ripe(), который будет проверять,
# что томат созрел (достиг последней стадии созревания) +
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список
# объектов класса Tomato.
# Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True,
# если все томаты из списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список
# томатов после сбора урожая +

# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены
# два динамических свойства: 1) name - передается параметром,
# является публичным и 2) _plant - принимает объект класса TomatoBush,
# является protected   +
# 3. Создайте метод work(), который заставляет садовника работать,
# что позволяет растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели.
# Если все садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5.Создайте статический метод knowledge_base(), который выведет в консоль
# справку по садоводству

# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

class Tomato:
    # Стадии созревания томата
    STATES = {
        1: 'empty',
        2: 'flower',
        3: 'yellow tomato',
        4: 'red tomato'
    }

    def __init__(self, index):
        self._index = index
        self._state = 1

    # Переход томата на следующую стадию созревания
    def grow(self):
        if self._state == 4:
            self._state += 1

    # Проверка, созрел ли наш томат
    def is_ripe(self):
        return self._state == 4


class TomatoBush:

    # Создаем генерато списка из объектов класса Tomato
    def __init__(self, number):
        self.tomatoes = [Tomato(i) for i in range(number)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли томаты созрели
    def all_are_ripe(self):
        return all(map(lambda tomato: tomato.is_ripe, self.tomatoes))

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Работа садовника, позволяющее томатам зреть
    def work(self):
        print('Gardener is working')
        self._plant.grow_all()
        print('Gardener finished')

    # Содовник собирает урожай
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Gardener give away all')
        else:
            print('Our plant is green')

    # Cтатический метод.
    @staticmethod
    def knowledge_base():
        print('Information about garden')


if __name__ == '__main__':
    Gardener.knowledge_base()
    # Вызовите справку по садоводству
    tomato_bush_obj = TomatoBush(4)
    # Создаём объекты классов Gardener
    gardener_obj = Gardener('Gardener', tomato_bush_obj)
    # Используя объект класса Gardener, поухаживайте за кустом с помидорами
    gardener_obj.work()
    # Попробуйте собрать урожай
    gardener_obj.harvest()
    gardener_obj.work()
    gardener_obj.harvest()