balls = ('F','FX','E','D','C', 'B', 'A')
grades = (1, 2, 3, 3, 4, 5, 5)
discriptions = ['неудовлетворительно',
                'неудовлетворительно',
                'достаточно',
                'удовлетворительно',
                'хорошо',
                'очень хорошо',
                'отлично']
                
ECTS = dict(zip(balls,                  list(zip(grades,discriptions))))

def get_grade(key):
    
    return ECTS.get(key, [None, None])[0]


def get_description(key):
  
    return ECTS.get(key, [None, None])[1]

print(get_grade('FX'))
print(get_description('FX'))
