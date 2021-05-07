def get_employees_by_profession(path, profession):
    with open(path, 'r') as f:
        print(f)
        lines = f.readlines()
    print(lines)
    lines = [line for line in lines if line.endswith(profession+'\n')]
    print(lines)
    s = ''.join(lines)
    print(s)
    return s.replace(profession, '').replace('\n', '').strip()

path = 'a.txt'
print(get_employees_by_profession(path, 'cook'))
