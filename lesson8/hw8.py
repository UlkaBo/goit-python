from collections import defaultdict
import datetime
users = [{'name': 'Bob', 'birthday': datetime.datetime(1990, 5, 10)},
         {'name': 'Nik', 'birthday': datetime.datetime(1990, 5, 11)},
         {'name': 'Ula', 'birthday': datetime.datetime(1990, 5, 12)},
         {'name': 'Nod', 'birthday': datetime.datetime(1990, 5, 13)},
         {'name': 'Cod', 'birthday': datetime.datetime(1990, 5, 14)},
         {'name': 'Dob', 'birthday': datetime.datetime(1990, 5, 15)},
         {'name': 'Mod', 'birthday': datetime.datetime(1990, 5, 15)},
         {'name': 'Ada', 'birthday': datetime.datetime(1990, 5, 16)},
         {'name': 'Leo', 'birthday': datetime.datetime(1990, 5, 18)},
         {'name': 'Oko', 'birthday': datetime.datetime(1990, 5, 18)},
         {'name': 'Sky', 'birthday': datetime.datetime(1990, 5, 19)},
         {'name': 'Via', 'birthday': datetime.datetime(1990, 5, 20)},
         {'name': 'Vud', 'birthday': datetime.datetime(1990, 5, 10)},
         {'name': 'God', 'birthday': datetime.datetime(1990, 5, 11)},
         {'name': 'Rom', 'birthday': datetime.datetime(1990, 5, 12)},
         {'name': 'Dog', 'birthday': datetime.datetime(1990, 5, 14)},
         {'name': 'Cat', 'birthday': datetime.datetime(1990, 5, 15)},
         {'name': 'Tor', 'birthday': datetime.datetime(1990, 5, 9)},
         {'name': 'Que', 'birthday': datetime.datetime(1990, 5, 9)},
         ]


def congratulate(us):
    # дата сегодня

    now = datetime.datetime.today()

    # порядковый номер текущей недели

    now_week = now.isocalendar()[1]

    # выбираю людей у которых дата рождения с измененным годом на текущий год
    # приходится на высчитанную неделю now_week
    # беру только имя и название дня недели

    users_now_week = [{'name': el['name'],
                       'day': el['birthday'].replace(now.year).strftime('%A')}
                      for el in us
                      if el['birthday'].replace(now.year).isocalendar()[1] == now_week]

    # словарь с ключом - название дня недели, и значением  - списком имен

    dct_lst = defaultdict(list)
    for eд in users_now_week:
        dct_lst[el['day']].append(el['name'])

    # субботу и воскресенье переношу в понедельник

    dct_lst['Monday'].extend(dct_lst['Saturday']+dct_lst['Sunday'])
    del dct_lst['Saturday'], dct_lst['Sunday']

    # печатаю

    for el in dct_lst:
        print(el+': ', *dct_lst[el])


def main():
    congratulate(users)


if __name__ == '__main__':
    main()
