def write_and_get_employees(employee_list, path):
    with open(path, 'w') as f:
        print(f)
        for el in employee_list:
            f.write('\n'.join(el)+'\n')
    print(f.closed)

    with open(path, 'r') as f:

        a = f.readlines()
    print(f.closed)

    return a


employee_list = [['Robert Stivenson, 28 years',
                  'Alex Denver, 30 years'], ['Drake Mikelsson, 19 years']]
write_and_get_employees(employee_list, 'hw6_2.txt')
