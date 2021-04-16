from pathlib import *
import sys

dict_list_files = {'images': [],
                   'movies': [],
                   'docs': [],
                   'musics': [],
                   'archs': [],
                   'unknows': []
                   }

dict_ext = {}

list_know = []
list_unknow = []


def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            # p = path.joinpath(el.name)  # p  = path / el.name
            parse_folder(path / el.name)
        else:
            if el.suffix in dict_ext.keys():
                list_know.append(el.suffix)
                name_list = dict_ext[el.suffix]
            else:
                list_unknow.append(el.suffix)
                name_list = 'unknows'
            #name_list = dict_ext.get(el.suffix, 'unknows')
            dict_list_files[name_list].append(el.name)


def main():
    dir_name = sys.argv[1]
    path_dir = Path(dir_name)
    # -------create a dictionary  - extantion : directory
    #        and create lists

    images = '.jpg .png .jpeg .svg'.split()
    movies = '.avi .mp4 .mov .mkv'.split()
    docs = '.doc .docx .txt .pdf .xlsx .pptx'.split()
    musics = '.mp3 .ogg .wav .amr'.split()
    archs = 'zip gz tar'.split()
    list_ext = ['images', 'movies', 'docs', 'musics', 'archs']

    for el in list_ext:
        l = eval(el)
        dict_ext.update(dict(zip(l, [el] * len(l))))

    # -------  end of create a dictionary

    parse_folder(path_dir)

    for k, v in dict_list_files.items():
        print(k, v)
    print(list_know)
    print(list_unknow)


if __name__ == '__main__':
    main()
