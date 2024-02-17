"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
"""


def dict_of_var(**kwargs) -> dict:
    my_dict = {}
    for key, value in locals()['kwargs'].items():
        try:
            my_dict[value] = key
        except:
            my_dict[str(value)] = key
    return my_dict


print(dict_of_var(e=4, c=['2', 4], r=321))
