from pathlib import *
import sys
import re
import shutil


# ---------create list translates latine

# create list ords of kirilic symbols
#  А-Я  Ґ Є І Ї  а-я  ґ є і ї
ords_kir = list(range(1040, 1072)) + [1168, 1028, 1030, 1031] + \
    list(range(1072, 1104)) + [1169, 1108, 1110, 1111]

lat_up = 'A B V G D E Zh Z Y Y K L M N O P R S T U F Kh Ts Ch Sh Shch _ Y _ E Yu Ya H Ye I Yi '
lat_low = lat_up.lower()
lat = (lat_up + lat_low).split()

# create dictionary from two lists
d_trunslit = dict(zip(ords_kir, lat))

# replace 'ъь' на ''
for i in [1066, 1068, 1098, 1100]:
    d_trunslit[i] = ''

# ------ конец создания словаря транслитерации

# ------ заготовки для создания словаря расширений

images = '.jpg .png .jpeg .svg'.split()
video = '.avi .mp4 .mov .mkv'.split()
documents = '.doc .docx .txt .pdf .xlsx .pptx'.split()
audio = '.mp3 .ogg .wav .amr'.split()
archives = '.zip .gz .tar'.split()
list_ext = ['images', 'video', 'documents', 'audio', 'archives']

# ------конец  заготовки для создания словаря расширений


def normalize(text: str):
    new_text = text.translate(d_trunslit)
    new_text = re.sub(r'[^\w ]', '_', new_text)
    return new_text


def parse_folder(path, path_dir, dict_ext):
    if not list(path.iterdir()):
        path.rmdir()
        return

    for el in path.iterdir():
        # запоминаю путь к файлу в текущей директории
        fromm = el

        #  нормализирую имя файла  + расширение
        #  если там имя дирректории, то suffix  будет ''
        name = normalize(el.stem) + el.suffix

        too = path / name
        # пересохраняю файл(директорию) с новым нормализированным именем
        fromm.rename(too)

        new_el = too
        # сейчас правильный (рабочий) путь к файлу(директории) - new_el, это объект Path

        if new_el.is_dir():

            # разные способы склеивания пути
            # p = path.joinpath(new_el.name)  # p  = path / new_el.name
            if name not in list_ext:
                parse_folder(new_el, path_dir, dict_ext)
        else:

            # если это архив, то добавляю к пути подпапку с именем new_el.stem
            if new_el.suffix in archives:
                too = path_dir / 'archives' / new_el.stem
                # распаковываю туда
                shutil.unpack_archive(str(new_el), str(too))
                # удаляю сам архив
                new_el.unlink()
            elif new_el.suffix in dict_ext:
                # запоминаю путь к файлу в директории, куда хочу перенести
                too = path_dir / dict_ext[new_el.suffix] / new_el.name
                fromm.rename(too)

    if not list(path.iterdir()):
        path.rmdir()
        return


def main():
    dir_name = sys.argv[1]
    path_dir = Path(dir_name)
    # -------create a dictionary  - extantion : directory
    #        and create directories

    dict_ext = {}

    if not (path_dir / 'unknows').exists():
        Path.mkdir(path_dir / 'unknows')
    for el in list_ext:
        l = eval(el)
        if not (path_dir / el).exists():
            Path.mkdir(path_dir / el)
        dict_ext.update(dict(zip(l, [el] * len(l))))

    # -------  end of create a dictionary

    parse_folder(path_dir,  path_dir, dict_ext)


if __name__ == '__main__':
    main()
