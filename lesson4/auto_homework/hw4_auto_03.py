def format_ingredients(items):
    a = ', '.join(items)
    i = a.rfind(',')
    if i == -1 :
        return ''.join(items)
    return a[:i] + ' и' + a[i+1:]

print(format_ingredients(['яйца 2шт']))
