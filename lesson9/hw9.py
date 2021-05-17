phone_book = {}


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
    data = data.replace('add ', '')
    if len(data.split()) == 2:
        name, phone = data.split()
        if name not in phone_book:
            phone_book[name] = phone
        else:
            raise Exception("This user already exist")
    else:
        raise Exception("Give me name and phone please")


@input_error
def change(data):
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
    str_phone_book = [' '.join(el) for el in phone_book.items()]
    return '\n'.join(str_phone_book)


@input_error
def good_bye(data):
    return "Good bye!"


@input_error
def ext(data):
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


@input_error
def choice_action(data):
    for command in ACTIONS:
        if data.startswith(command):
            return ACTIONS[command]
    raise Exception("Give me a correct command please")


def main():
    while True:
        data = input()

        func = choice_action(data)
        if isinstance(func, Exception):
            print(func)
            continue
        result = func(data)
        if result == 'break':
            break
        elif result:
            print(result)
        if result == 'Good bye!':
            break


if __name__ == '__main__':
    main()
