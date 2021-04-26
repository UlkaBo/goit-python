def navigate_clients(path, code):
    with open(path, 'r') as f:
        f.seek(len(str(code))+1)
        a = f.readline()

    f.close()
    return a


print(navigate_clients('a.txt', '23423423'))
