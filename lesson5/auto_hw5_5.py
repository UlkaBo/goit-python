import re

dict_cods = dict(zip('81 65 886 380'.split(),
                     'JP SG TW UA'.split()))


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    dict_phones = dict()
    for tel in list_phones:
        tel = sanitize_phone_number(tel)
        for cod, country in dict_cods.items():
            if tel.startswith(cod):
                dict_phones[country] = dict_phones.get(country, [])+[tel]
                break
        else:
            dict_phones['UA'] = dict_phones.get('UA', [])+[tel]

    return dict_phones


list_phones = ['+386445434', '81564', ' 88()', '+6533322']
print(get_phone_numbers_for_countries(list_phones))
