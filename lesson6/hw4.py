from pathlib import *
import sys


def parse_folder(path, path_dir, dict_ext):
    for el in path.iterdir():
        if el.is_dir():
            # p = path.joinpath(el.name)  # p  = path / el.name
            parse_folder(path / el.name, path_dir, dict_ext)
        else:
            fromm = path / el.name
            too = path_dir / dict_ext.get(el.suffix, 'unknows') / el.name
            fromm.rename(too)


def main():
    dir_name = sys.argv[1]

    # -------create a dictionary  - extantion : directory
    #        and create directories

    images = '.jpg .png .jpeg .svg'.split()
    movies = '.avi .mp4 .mov .mkv'.split()
    docs = '.doc .docx .txt .pdf .xlsx .pptx'.split()
    musics = '.mp3 .ogg .wav .amr'.split()
    archs = 'zip gz tar'.split()
    list_ext = ['images', 'movies', 'docs', 'musics', 'archs']

    dict_ext = {}
    path_dir = Path(dir_name)
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
