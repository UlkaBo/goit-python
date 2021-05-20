def generator_numbers(string=""):
    import re
    lst_numbers = re.findall('\d+', string)
    for number in lst_numbers:
        yield number


def sum_profit(string):
    x = generator_numbers(string)
    return sum(x)


sum_profit('dfgdfg45 dfgdf44 dgdfg33edss2')
