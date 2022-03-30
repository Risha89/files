import os


def sort_files():
    list_of_files = []
    for el in os.listdir():
        if el.endswith('txt'):
            list_of_files.append(el)
    files_dict = {}
    for el in list_of_files:
        with open(el, 'r', encoding='utf-8') as text:
            files_dict[el] = len(text.readlines())
    a = sorted(files_dict.items(), key=lambda item: item[1])
    q = {}
    for el in a:
        q[el[0]] = el[1]
    return q


def read_write(path: str, mode: str, encoding='utf-8'):
    with open(path, mode) as file:
        for el in sort_files():
            with open(el, 'r', encoding='utf-8') as f:
                file.write(el + '\n')
                file.write(str(sort_files()[el]) + '\n')
                for line in f:
                    file.write(line)
                file.write('\n')


read_write('C:/new/final/final.txt', 'w')
