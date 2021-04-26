from pathlib import *
import sys
import re
import shutil


d_trunslit = {1040: 'A', 1041: 'B', 1042: 'V', 1043: 'G', 1044: 'D', 1045: 'E', 1046: 'Zh', 1047: 'Z',
              1048: 'Y', 1049: 'Y', 1050: 'K', 1051: 'L', 1052: 'M', 1053: 'N', 1054: 'O', 1055: 'P',
              1056: 'R', 1057: 'S', 1058: 'T', 1059: 'U', 1060: 'F', 1061: 'Kh', 1062: 'Ts', 1063: 'Ch',
              1064: 'Sh',
              1065: 'Shch',
              1066: '', 1067:
              'Y', 1068: '', 1069: 'E', 1070: 'Yu', 1071: 'Ya',
              1168: 'H', 1028: 'Ye', 1030: 'I', 1031: 'Yi',
              1072: 'a', 1073: 'b', 1074: 'v', 1075: 'g', 1076: 'd', 1077: 'e', 1078: 'zh', 1079: 'z',
              1080: 'y', 1081: 'y', 1082: 'k', 1083: 'l', 1084: 'm', 1085: 'n', 1086: 'o', 1087: 'p',
              1088: 'r', 1089: 's', 1090: 't', 1091: 'u', 1092: 'f', 1093: 'kh', 1094: 'ts', 1095: 'ch',
              1096: 'sh', 1097: 'shch', 1098: '', 1099: 'y', 1100: '', 1101: 'e', 1102: 'yu', 1103: 'ya',
              1169: 'h', 1108: 'ye', 1110: 'i', 1111: 'yi'}


images = ['.jpg', '.png', '.jpeg', '.svg']
video = ['.avi', '.mp4', '.mov', '.mkv']
documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
audio = ['.mp3', '.ogg', '.wav', '.amr']
archives = ['.zip', '.gz', '.tar']

list_ext = ['images', 'video', 'documents', 'audio', 'archives']

dict_ext = {'.jpg': 'images', '.png': 'images', '.jpeg': 'images', '.svg': 'images',
            '.avi': 'video', '.mp4': 'video', '.mov': 'video', '.mkv': 'video',
            '.doc': 'documents', '.docx': 'documents', '.txt': 'documents',
            '.pdf': 'documents', '.xlsx': 'documents', '.pptx': 'documents',
            '.mp3': 'audio', '.ogg': 'audio', '.wav': 'audio', '.amr': 'audio',
            '.zip': 'archives', '.gz': 'archives', '.tar': 'archives'}


def normalize(text):
    new_text = text.translate(d_trunslit)
    new_text = re.sub(r'[^\w ]', '_', new_text)
    return new_text


def parse_folder(path, path_dir):
    if not list(path.iterdir()):
        path.rmdir()
        return

    for el in path.iterdir():

        path1 = el

        name = normalize(el.stem) + el.suffix

        path2 = path / name

        path1.rename(path2)

        new_el = path2

        if new_el.is_dir():
            if name not in list_ext:
                parse_folder(new_el, path_dir)
        else:

            if new_el.suffix in archives:
                path2 = path_dir / 'archives' / new_el.stem

                shutil.unpack_archive(str(new_el), str(path2))
                new_el.unlink()
            elif new_el.suffix in dict_ext:
                path2 = path_dir / dict_ext[new_el.suffix] / new_el.name
                path1.rename(path2)

    if not list(path.iterdir()):
        path.rmdir()
        return


def main():
    dir_name = sys.argv[1]
    path_dir = Path(dir_name)
    #   creating directories

    for el in list_ext:

        if not (path_dir / el).exists():
            Path.mkdir(path_dir / el)

    # end of creating  directories

    parse_folder(path_dir,  path_dir)


if __name__ == '__main__':
    main()
