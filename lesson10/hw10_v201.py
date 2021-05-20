from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone) -> None:
        self.phone = phone


class AddressBook(UserDict):
    def add_record(self, record):
        self[record.name.name] = record


class Record():

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, phone):
        pass
