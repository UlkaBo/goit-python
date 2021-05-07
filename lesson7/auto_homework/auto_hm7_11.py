def sequence_buttons(string):
    letters = '.,?!:abcdefghijklmnopqrstuvwxyz '
    digits = [1,11,111,1111,11111,
             2,22,222,
             3,33,333,
             4,44,444,
             5,55,555,
             6,66,666,
             7,77,777,7777,
             8,88,888,
             9,99,999,9999,0]
    map_tr = {ord(k) : str(v) for k,v in zip(letters, digits)}
    print(len(letters),len(digits))
    print(map_tr)
    return string.lower().translate(map_tr)
        
        
print(sequence_buttons('Hi there!'))
