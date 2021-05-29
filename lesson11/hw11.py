from collections import UserDict
import datetime
import re

pattern_phone = '\d{3,}'


class Field:
    def __init__(self, value):
        self.__value = self.value(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    pass


class Phone(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):

        # проверка данных на корректность.
        # паттерн  pattern_phone указан в начале программы
        if re.fullmatch(pattern_phone, new_value):
            self.__value = new_value

        else:
            print('Phone number is wrong')


class Birthday(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):

        # предполагаю, что new_value  может быть записан с любыми разделителями
        # извлекаю оттуда только числа
        numbers_date = re.split(r'[\.,\- /:]+', new_value)

        # преобразую в кортеж чисел
        numbers_date = tuple(map(int, numbers_date))

        try:
            # если из этих чисел получается дата
            date_birthday = datetime.datetime(*numbers_date).date()

            # и эта дата не из будущего
            if date_birthday >= datetime.datetime.now():
                print('Date from future')
                return

            # присваиваем новое значение даты
            self.__value = date_birthday

        except:
            print('Date is wrong')


class AddressBook(UserDict):

    def add_record(self, record):
        self[record.name.value] = record

    def __next__(self):
        if self.i >= len(self):
            raise StopIteration

        # перебирать self, например self.items()  здесь нельзя,
        # уходит в рекурсивный вызов
        # только через self.data

        # Надо получить срез от i-го до i+N-го елемента
        # для этого делаю список
        lst_items = list(self.data.items())

        # делаю срез и сразу преобразую полученный кусок в словарь
        cuter_items = dict(lst_items[self.i: self.i + self.N])

        # передвигаю self.i
        self.i += self.N

        #  возвращаю "срезанный" словарь
        return cuter_items

    def __iter__(self, N=1):
        # внутренний счетчик, который обнуляется при каждом новом создании итератора
        self.i = 0

        # Количество записей, выводимых на каждой итеррации. Не понятно как этот аргумент будет передаваться
        self.N = N

        # можно ли возвращать не только self ? А, например, кусок словаря ?
        return self


class Record():

    def __init__(self, name, phone=[], birthday=None):
        self.name = name
        self.phones = phone
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, phone):
        pass

    def days_to_birthday(self):
        now = datetime.datetime.today()

        # отдельный случай  - день рождения 29 февраля
        # чтобы избежать столкновения с 29/2  будем  брать в расчет
        # день на день позже дня рождения.
        # после всех вычислений мы  отнимем один день
        if (self.birthday.day, self.birthday.month) == (29, 2):
            bd = self.birthday + datetime.timedelta(day=1)
        else:
            bd = self.birthday
        # получаю дату дня  рождения в этому году
        bd_that_year = bd.replace(year=now.year)

        # дельта от дня рождения до сегодня
        delta = bd_that_year - now

        # если она отрицательна, то значит др в этом году уже прошел
        if delta <= 0:

            # надо брать дату дня рождения следующего года
            bd_that_year = bd_that_year.replace(year=now.year+1)

            # дельта от дня рождения в следующем году до сегодня
            delta = bd_that_year - now

        if (self.birthday.day, self.birthday.month) == (29, 2):
            return delta.days - 1
        return delta.days
