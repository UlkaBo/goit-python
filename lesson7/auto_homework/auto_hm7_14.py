def to_indexed(start_file, end_file):
    with open(start_file, 'r') as f:
        lines = f.readlines()
      
    n_l = [f'{i}: {lines[i]}' for i in range(len(lines))]
    print(lines)
    print(n_l)
    with open(end_file, 'w') as f:
        f.writelines(n_l)

to_indexed('a.txt', 'b.txt')
