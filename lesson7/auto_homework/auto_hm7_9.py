def all_sub_lists(data):
    sublists = [[]]
    len_ = len(data)
    for i in range(1, len_+1):
        for beg in range(len_ - i+1):
            sublists.append(data[beg:beg+i])
    return sublists
d = [4, 6, 1, 3]
print(all_sub_lists(d))
