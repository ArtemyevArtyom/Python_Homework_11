"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

strings = ['разработка', 'администрирование', 'protocol', 'standard']
my_list = []


def byte_function():
    print('Преобразование в байтовое представление:')
    for el in strings:
        new_form = str.encode(el, encoding='utf-8')
        print(type(new_form), {new_form})
        my_list.append(new_form)


def string_function():
    print('Преобразование обратно в строковое представление:')
    for element in my_list:
        str_form = bytes.decode(element, encoding='utf-8')
        print(type(str_form), str_form)


byte_function()
print()
string_function()
