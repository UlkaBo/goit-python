import pickle
import sys
import os.path

from classes_hw12 import AddressBook, Record, Name, Phone, Birthday


file = 'data.bin'


# декоратор  - обработчик ошибок
def input_error(func):
    def hundler(data):
        try:
            result = func(data)
        except Exception as e:
            return e
        return result
    return hundler


@input_error
def hello(data):
    print("How can I help you?")


@input_error
def add_ph(data):
    # функция, которая добавляет номер телефона по имени
    # в data  должна  прийти строка, которая начинается с "add "
    # и содержит еще два "слова"  - имя  и телефон
    # "add ph " удаляется сразу
    data = data.replace('add ph ', '')
    #  действительно ли там есть два "слова" ?
    if len(data.split()) == 2:
        name, phone = data.split()

        if name not in phone_book:
            # добавляем в phone_book  новую запись,
            # предварительно долго и нудно ее создаем

            n = Name(name)
            ph = Phone(phone)
            rec = Record(name=n, phone=ph)

            phone_book.add_record(rec)
            # какой прищепкой цеплять сюда день рождения?

        else:
            # если запись с таким именем уже есть, то добавляем юзеру еще один телефон
            phone = Phone(phone)
            phone_book[name].add_phone(phone)

    else:
        raise Exception("Give me name and phone please")


@input_error
def add_bd(data):
    # функция, которая добавляет день рождения по имени
    # в data  должна  прийти строка, которая начинается с "add "
    # и содержит еще два "слова"  - имя  и день рождения
    # "add bd " удаляется сразу
    data = data.replace('add bd ', '')

    #  действительно ли там есть два "слова" ?
    if len(data.split()) == 2:
        name, birthday = data.split()
        bd = Birthday(birthday)

        # если записи с таким именем нет
        if name not in phone_book:
            # добавляем в phone_book  новую запись,
            # предварительно долго и нудно ее создаем

            n = Name(name)

            rec = Record(name=n, birthday=bd)

            phone_book.add_record(rec)

        # если запись такая есть, но др пустое, то заполняем его
        elif phone_book[name].birthday.value == None:
            phone_book[name].change_birthday(bd)

        #  если запись такая уже есть
        else:
            raise Exception("Abonent already has a birthday")

    else:
        raise Exception("Give me name and brthday please")


@input_error
def change_ph(data):
    #   чтобы изменить телефон. должна получить три слова
    #   name, phone, new_phone
    data = data.replace('change ph ', '')
    if len(data.split()) == 3:
        name, phone, new_phone = data.split()
        if name in phone_book:
            #  здесь передаю в метод объекты только потому что везде передаю в методы обекты.
            #  Хотя здесь лучше бы передавать строки . Все-равно внутри метода
            #  мне нужно вытащить строки. И можно было бы заменить в существующем объекте Phone
            #  существующее поле value. Но я же уже передала объект, поэтому буду там в записи
            #  менять объект Phone.
            #  вобщем криво. Мне нравится. Как правильно ?
            phone_book[name].change_phone(Phone(phone), Phone(new_phone))
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Give me name and phone please")


@input_error
def change_bd(data):
    #   изменить день рождения. должна получить два слова
    #   name,  new_birthday
    data = data.replace('change bd ', '')
    if len(data.split()) == 2:
        name,  new_birthday = data.split()
        if name in phone_book:
            new_birthday = Birthday(new_birthday)
            phone_book[name].change_birthday(new_birthday)
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Give me name and birthday, please")


@input_error
def phone(data):
    # простая функция поиска записи  по  имени, то есть по ключу
    data = data.replace('phone ', '')
    if len(data.split()) == 1:
        name = data
        if name in phone_book:
            return phone_book[name]
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Give me only name")


@input_error
def show_all(data):
    data = data.replace('show all', '')
    if len(data.split()) == 1:
        # проверка   - если параметр  N задан некорректно задаем ему 1
        try:
            N = int(data)
        except:
            N = 1
    else:
        # если не задан параметр N  считаем N равным длине словаря
        N = len(phone_book.data)

    # вызывает метод итератор из AddressBook
    for el in phone_book.iterator(N):
        print(el)
        print('----------')

    # выполнить требование, чтобы все принты были в main  не получается
    # поэтому в return  идет бессмысленная строка. Щоб була...
    return 'it\'s all'


@input_error
def find(data):
    #  функция поиска записей по части имени или части телефона
    data = data.replace('find ', '')
    if len(data.split()) == 1:
        # вызывается метод класса AddressBook
        result = phone_book.full_search(data)
        return result


@input_error
def good_bye(data):
    # функция окончания работы и сохранения данных
    #
    with open(file, 'wb') as f:
        pickle.dump(phone_book, f)
    return "Good bye!"


ACTIONS = {
    'hello': hello,
    'add ph': add_ph,
    'add bd': add_bd,
    'change ph': change_ph,
    'change bd': change_bd,
    'phone': phone,
    'show all': show_all,
    'find ': find,
    'good bye': good_bye,
    'close': good_bye,
    'exit': good_bye,
    '.': good_bye,
}


@input_error
def choice_action(data):
    for command in ACTIONS:
        if data.startswith(command):
            return ACTIONS[command]
    raise Exception("Give me a correct command please")


if __name__ == '__main__':

    phone_book = AddressBook()
    # открываю файл данных если он есть.

    if os.path.isfile(file):
        with open(file, 'rb') as f:
            phone_book = pickle.load(f)
    #  если его нет, то phone_book будет новым экземляром AddressBook

    while True:
        text = ''' You can:
        hello, good bye, close, exit, . - understandably
        add ph <name> <phone>
        add bd <name> <birthday>
        show all  <N>    - show all abonent, N - number abonents in page
        phone <name>  - show all phone this abonent
        change ph <name> <phone> <new_phone>
        change bd <name> <new_birthday>
        find <str>    - seek all records where is finding <str>
        '''
        print(text)
        data = input()

        func = choice_action(data)
        if isinstance(func, Exception):
            print(func)
            continue
        result = func(data)
        if result:
            print(result)
        if result == 'Good bye!':
            break
