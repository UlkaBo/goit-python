import pickle
import sys
import os.path
from tkinter import *

from class_hw12 import AddressBook, Record, Name, Phone, Birthday

phone_book = {}
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
def add(data):
    # функция, которая добавляет номер телефона по имени
    # в data  должна  прийти строка, которая начинается с "add "
    # и содержит еще два "слова"  - имя  и телефон
    # "add " удаляется сразу
    data = data.replace('add ', '')
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
            phone_book[name].add_phone(phone)

    else:
        raise Exception("Give me name and phone please")


@input_error
def change(data):
    #   судьба этой функции неясна
    data = data.replace('change ', '')
    if len(data.split()) == 2:
        name, phone = data.split()
        if name in phone_book:
            phone_book[name] = phone
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Give me name and phone please")


@input_error
def phone(data):
    # метод поиска записи  по  имени
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
    # вызывает метод итератор из AddressBook
    #
    for el in phone_book.iterator(5):
        print(el)
        print('----------')
    # выполнить требование, чтобы все принты были в main  не получается
    # поэтому в return  идет бессмысленная строка. Щоб була...
    return 'it\'s all'


@input_error
def good_bye(data):
    # функция окончания работы и сохранения данных
    #
    with open(file, 'wb') as f:
        pickle.dump(phone_book, f)
    return "Good bye!"


ACTIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
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


def main():
    global phone_book
    phone_book = AddressBook()
    # открываю файл данных если он есть.

    if os.path.isfile(file):
        with open(file, 'w') as f:
            phone_book = pickle.load(f)
    #  если его нет, то phone_book будет новым экземляром AddressBook
    # это будет  global . Наверное так плохо делать.
    # Как правильно? Передавать phone_book  в каждую функцию?

    # -----------GUI tkinter-------------

    # ----------end GUI tkinter--------------

    while True:
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


if __name__ == '__main__':
    main()
