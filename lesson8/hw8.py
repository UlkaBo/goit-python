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

    now = datetime.datetime.today()

    #  количество дней назад была суббота

    delta_back = datetime.timedelta(now.weekday()+2)

    # список дат с последней субботы до пятницы этой недели

    lst_days = [now - delta_back + datetime.timedelta(i) for i in range(7)]

    # создаю словарь полученных дат  в виде {(месяц, день) : название дня недели, ...}

    dct_tpl_days = {(el.month, el.day): el.strftime('%A') for el in lst_days}

    # словарь  - списки именников по дням недели. Ключ - название для недели

    dct_lst_congr = defaultdict(list)
    for el in us:
        month_day = (el['birthday'].month, el['birthday'].day)
        if month_day in dct_tpl_days:
            dct_lst_congr[dct_tpl_days[month_day]].append(el['name'])

    # субботу и воскресенье переношу в понедельник

    dct_lst_congr['Monday'].extend(
        dct_lst_congr['Saturday']+dct_lst_congr['Sunday'])
    del dct_lst_congr['Saturday'], dct_lst_congr['Sunday']

    # печатаю

    for el in dct_lst_congr:
        print(el+': ', ', '.join(dct_lst_congr[el]))


def main():
    congratulate(users)


if __name__ == '__main__':
    main()
