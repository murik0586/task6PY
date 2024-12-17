import re

def remove_repeated_words(some_string):

    pattern = r'\b(\w+)\b(?:\s+\1\b)+'
    result = re.sub(pattern, r'\1', some_string)
    return result

some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений'
print(remove_repeated_words(some_string))
