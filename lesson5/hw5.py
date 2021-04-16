import sys
import re


# А-Я  Ґ Є І Ї  а-я  ґ є і ї
ords_kir = list(range(1040, 1072)) + [1168, 1028, 1030, 1031] + \
    list(range(1072, 1104)) + [1169, 1108, 1110, 1111]
lat_up = 'A B V G D E Zh Z Y Y K L M N O P R S T U F Kh Ts Ch Sh Shch _ Y _ E Yu Ya H Ye I Yi '
lat_low = lat_up.lower()
lat = (lat_up + lat_low).split()
d_trunslit = dict(zip(ords_kir, lat))


def noramlize(text: str):
    new_text = text.translate(d_trunslit)
    new_text = re.sub(r'[^\w ]', '_', new_text)
    return new_text


def main():
    st = sys.argv[1]
    print(noramlize(st))


if __name__ == "__main__":
    main()
