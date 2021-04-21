CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for cir, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cir)] = lat
    TRANS[ord(cir.upper())] = lat.upper()

print(TRANS)


def translate(name):

    new_name = name.translate(TRANS)
    return new_name


print(translate("вамипауж жуаі уйха вВІ ві"))
