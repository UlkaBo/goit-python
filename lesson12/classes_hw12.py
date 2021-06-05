from collections import UserDict
import datetime
import re
import copy

pattern_phone = '\d{3,}'


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):

    def __init__(self, value):
        self.value = value


class Phone(Field):

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):

        # проверка данных на корректность.
        # паттерн  pattern_phone указан в начале программы
        # if re.fullmatch(pattern_phone, new_value):
        # усилием воли было принято решение не применять проверку на корректность
        # просто из строки удалить  все не цифры
        # если количество цифр меньше шести телефон не записывается
        new_value = re.sub(r'[^\d]', '', new_value)
        if len(new_value) > 6:
            self.__value = new_value

        else:
            print('Phone number so short')
            self.__value = None


class Birthday(Field):

    def __init__(self, value):
        self.value = value

    '''
    def __init__(self. value):
        self.__value = 0
        self.value = value
    '''

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        # предполагаю, что new_value  может быть записан с любыми разделителями
        # извлекаю оттуда только числа
        numbers_date = re.findall(r'\d+', str(new_value))

        # если передали None , или там не три числа
        # значит создаем объект с value = None
        if len(numbers_date) != 3:
            self.__value = None

        # преобразую в кортеж чисел
        numbers_date = tuple(map(int, numbers_date))

        try:
            # если из этих чисел получается дата
            date_birthday = datetime.datetime(*numbers_date).date()

            # и эта дата не из будущего
            if date_birthday >= datetime.datetime.today().date():
                print('Date from future')
                self.__value = None
                return

            # присваиваем новое значение даты
            self.__value = date_birthday

        except:
            print('Date is wrong')
            self.__value = None


class Record():

    def __init__(self, name, phone='', birthday=Birthday(None)):
        self.name = name
        self.phones = [phone]
        self.birthday = birthday

    def __str__(self):
        result = ''
        result += f"name - {self.name.value} "
        if self.birthday:
            result += f"birthday - {str(self.birthday.value)} "
        result += f"phones - {', '.join([phone.value for phone in self.phones])}"
        return result

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, phone, new_phone):
        #  поиск по объекту Phone  не работает, потому что   ищет вхождение,
        '''
        try:
            idx = self.phones.index(phone)
            self.phones[idx] = new_phone
        except:
            raise Exception("Phone is not found")
        '''
        # а это is . Объект созданный с теми же данными будет новым объектом
        # Поэтому будем искать value объекта  .

        for i, el in enumerate(self.phones):
            if phone.value == el.value:
                self.phones[i] = new_phone
                break
        else:
            raise Exception("Phone is not found")

    def change_birthday(self,  new_birthday):
        if new_birthday.value != None:
            self.birthday = new_birthday
        else:
            raise Exception("New birthday is not correct")

    def days_to_birthday(self):
        now = datetime.datetime.today().date()

        # отдельный случай  - день рождения 29 февраля
        # чтобы избежать столкновения с 29/2  будем  брать в расчет
        # день на день позже дня рождения.
        # после всех вычислений мы  отнимем один день
        if (self.birthday.value.day, self.birthday.value.month) == (29, 2):
            bd = self.birthday.value + datetime.timedelta(days=1)
        else:
            bd = self.birthday.value

        # получаю дату дня  рождения в этому году
        bd_that_year = bd.replace(year=now.year)

        # дельта от дня рождения до сегодня
        delta = bd_that_year - now

        # если она отрицательна, то значит др в этом году уже прошел
        if delta.days <= 0:

            # надо брать дату дня рождения следующего года
            bd_that_year = bd_that_year.replace(year=now.year+1)

            # дельта от дня рождения в следующем году до сегодня
            delta = bd_that_year - now

        if (self.birthday.value.day, self.birthday.value.month) == (29, 2):
            return delta.days - 1
        return delta.days


class AddressBook(UserDict):

    # два следующих метода  - инструкции для сериализации
    # и десериализации  экземпляра класса  AddressBook
    # ----------------------------------
    def __getstate__(self):
        # deepcopy  для перестраховки.
        atr = copy.deepcopy(self.__dict__)
        return atr

    def __setstate__(self, atr):
        self.__dict__ = atr
    # -----------------------------------

    def add_record(self, record):
        '''
        немудреный метод для добавления одного элемента
        в словарь экземпляра
        record -  объект   класса Record, содержащий поля - 
        name - объект класса Name
        phones -   список объектов класса Phone
        birthday - объект класса  Birthday
        '''
        self[record.name.value] = record

    def full_search(self, user_or_phone):
        result = ''

        for rec in self.data.values():
            #  сначала ищу среди имен
            if user_or_phone in rec.name.value:
                result += str(rec)

            # потом ищу в телефонах
            # для этого удаляю все символы кроме цифр
            dig_user_or_phone = re.sub(r'[\D]', '', user_or_phone)
            if len(dig_user_or_phone) > 3:
                for phone in rec.phones:
                    if dig_user_or_phone in phone.value:
                        result += str(rec)

        return result

    def iterator(self, N):
        '''
        метод возвращает строку из нескольких записей

        Количество записей, выводимых на каждой итеррации - N
        Надеюсь этот аргумент будет передаваться именно в этот метод
        '''
        self.N = N
        self.i = 0
        new_iter = self
        while self.i < len(self.data):
            # получаем кусок словаря
            x = next(new_iter)
            # надо его развернуть в читабельный вариант
            lst = []
            for name, rec in x.items():
                lst.append(
                    f'{rec.name.value} : bd - {rec.birthday.value}, phone - {", ".join([phone.value for phone in rec.phones])}')
            yield '\n'.join(lst)

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
        # можно ли возвращать не только self ? А, например, кусок словаря ?
        return self
    '''
    def __str__(self):
        return '\n'.join(list(self.data.items()))
    '''


if __name__ == "__main__":

    ad_b = AddressBook()
    n = Name('Ya')
    tel = Phone('56432')
    bd = Birthday('1975-02-26')
    rec = Record(n, tel, bd)

    rec.birthday = Birthday('2000-02-29')
    print(rec.days_to_birthday())
    rec.add_phone(Phone('12344535'))
    ad_b.add_record(rec)

    n = Name('Yaa')
    tel = Phone('5-6432')
    bd = Birthday('2001-02-29')
    rec = Record(n, tel, bd)
    ad_b.add_record(rec)

    n = Name('Yab')
    tel = Phone('56432')
    bd = Birthday('1975 2-262')
    rec = Record(n, tel, bd)
    ad_b.add_record(rec)

    n = Name('Yac')
    tel = Phone('56679898432')
    bd = Birthday('2022-02-26')
    rec = Record(n, tel, bd)
    ad_b.add_record(rec)

    n = Name('Yad')
    tel = Phone('56    432')
    bd = Birthday('1975/02//26')
    rec = Record(n, tel, bd)
    ad_b.add_record(rec)
    x = ad_b.iterator(2)
    y = next(x)
    print(y)
    y = next(x)
    print(y)
    input()
