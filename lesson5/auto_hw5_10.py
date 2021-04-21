import re


def find_word(text, word):
    result = re.search(word, text)
    answer = {
        'result': False,
        'first_index': None,
        'last_index': None,
        'search_string': word,
        'string': text
    }
    if result:
        answer = {
            'result': True,
            'first_index': result.start(),
            'last_index': result.end(),
            'search_string': word,
            'string': text
        }
    return answer


print(find_word('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.', 'Python'))
