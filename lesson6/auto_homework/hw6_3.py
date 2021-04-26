def add_order(order, path):
    with open(path, 'a') as f:
        f.write('\n' + order)

    with open(path, 'r') as f:
        a = f.readlines()

    s = [1 for el in a if el.split(':')[1] == 'active']
    return sum(s)


def add_order(order, path):
    import os
    if os.path.exists(path):
        order = '\n' + order
    f = open(path, 'a')
    f.write(order)

    f.close()

    with open(path, 'r') as f:
        a = f.readlines()

    f.close()
    print(a)
    s = [el for el in a if el != '\n' and el.split(':')[1].strip() == 'active']
    print(s)
    return s


def add_order(order, path):
    import os
    if os.path.exists(path):
        order = '\n' + order
    f = open(path, 'a')
    f.write(order)

    f.close()

    with open(path, 'r') as f:
        a = f.read()

    f.close()
    return a.count(':active')


print(add_order('ss:not active', 'b.txt'))
