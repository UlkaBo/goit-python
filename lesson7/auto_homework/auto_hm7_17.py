def encode(data):
    if len(data) < 2 : return list(data)
    i = 0
    while i+1 < len(data) and data[0] == data[i+1] :
        i += 1
    return [data[0], i+1] + encode(data[i+1:]) 

d = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
print(encode(d))
