'''
первый вариант дз10.
реализовывала добавление в record телефонов как полей.
добавление работает 
change  не работает.
''''

from collections import UserDict


class Field:
    pass


class Name(Field):
    value = ''


class Phone(Field):
    phone = ''


class AddressBook(UserDict):
    def add_record(self, record):
        self[record.name.value] = record


class Record():
    name = Name()

    def add_phone_to_list(self,  phone):
        if 'phones' not in vars(self):
            self.phones = []
        ph = Phone()
        ph.phone = phone
        self.phones.append(ph)

    def add_phone_as_field(self,  phone):
        dct_phones = self.extract_phones()
        if phone not in dct_phones.values():
            new_name_phone = f'phone_{len(dct_phones)}'
            vars(self)[new_name_phone] = Phone()
            vars(self)[new_name_phone].phone = phone
        else:
            raise Exception("User already has this phone ")

    def extract_phones(self) -> dict:

        return {el: vars(self)[el] for el in vars(self) if type(vars(self)[el]) == Phone}

    def change(self, phone):
        dct_phones = self.extract_phones()
        print([(k, vars(v)) for k, v in (vars(self).items())])
        what_phone = 'phone_' + \
            input('What phone you want to change(1/2/...) : ').strip()
        old_phone = vars(self)[what_phone]
        print(f'you want to change {old_phone} to {phone}')
        vars(self)[what_phone] = phone


phone_book = AddressBook()


def input_error(func):
    def hundler(command, data):
        try:
            result = func(command, data)
        except Exception as e:
            return e
        return result
    return hundler


@ input_error
def hello(data):
    print("How can I help you?")


@ input_error
def add(command, data):
    print(data)
    if len(data) == 2:
        name, phone = data

        if name not in phone_book:
            record = Record()
            record.name.value = name
            phone_book.add_record(record)

        else:
            record = phone_book[name]

        # record.add_phone_to_list(phone) or
        record.add_phone_as_field(phone)

    else:
        raise Exception("Give me two argument  - name and phone,  please")


@ input_error
def change(command, data):
    if len(data) == 2:
        name, phone = data
        if name in phone_book:
            phone_book[name] = phone
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Give me name and phone please")


@ input_error
def phone(command, data):
    if len(data) == 1:
        name = data[0]
        if name in phone_book:
            return vars(phone_book[name])
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Give me only name")


@ input_error
def show_all(command, data):
    str_phone_book = [str(vars(el).items()) for el in phone_book.items()]
    return '\n'.join(str_phone_book)


@ input_error
def good_bye(command, data):
    return "Good bye!"


@ input_error
def ext(command, data):
    return 'break'


ACTIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'good bye': good_bye,
    'close': good_bye,
    'exit': good_bye,
    '.': ext
}


@ input_error
def choice_action(command, data):
    return ACTIONS[command]
    raise Exception("Give me a correct command please")


def main():
    while True:
        data = input()
        command = 'unknown'
        for com in ACTIONS:
            if data.startswith(com):
                command = com
                data = data.replace(com, '')
                break
        data = data.split()
        # command, *data = (data.strip() or 'nothing').split()
        func = choice_action(command, data)
        if isinstance(func, Exception):
            print(func)
            continue
        result = func(command, data)
        if result == 'break':
            break
        elif result:
            print(result)
        if result == 'Good bye!':
            break


if __name__ == '__main__':
    main()
