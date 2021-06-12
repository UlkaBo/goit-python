from collections import UserDict
from datetime import date, datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record

    def iterator(self,N):
        res = ''
        k = 0
        while k < N:
            res += next(self).value.__repr__()
            k += 1
            print(res)
        yield res

class Field():
    pass

class Name(Field):
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

class Phone(Field):
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        trans_phone = phone.translate(str.maketrans('     ', '+() -'))
        if trans_phone.isdigit():
            self.__phone = trans_phone
        else:
            raise ValueError('Typed phone number is not correct. Try again!')

class Birthday(Field):
    def __init__(self, birthday):
        #self.__birthday = None
        try:
            self.__birthday = datetime.strptime(bithday, '%d-%m-%Y')
        except ValueError:
            print(f'Date is not correct. Ente date in format: (day)-(month)-(Year)')
            self.__birthday = None

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, new_date):
        try:
            check_date = datetime.strptime(new_date, '%d-%m-%Y')
        except ValueError:
            print(f'Date is not correct. Ente date in format: (day)-(month)-(Year)')
            return self
        if check.date < datetime.now():
            self.__birthday = check_date.date()
        else:
            print('Birthday can not be in future')

class Record(Field):

    def __init__(self, name, birthday = None):
        self.name = name
        self.phone_list = []
        self.birthday = birthday

    def add_phone(self, phone):
        self.phone_list.append(phone)

    def delete_phone(self, phone):
        self.phone_list.remove(phone)

    def change_phone(self, old_phone, new_phone):
        ind = self.phone_list.index(old_phone)
        self.phone_list.remove(phone)
        self.phone_list.insert(ind, new_phone)

    def days_to_birthday(self):
        if date.today() > self.birthday.replace(year=date.today().year):
            return (self.birthday.replace(year=date.today().year + 1) - date.today()).days
        return (self.birthday.replace(year=date.today().year) - date.today()).days


