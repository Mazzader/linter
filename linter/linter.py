import re

from linter.models import Document

res_len_str = {}
res = {}
reg_exp_brace_in_func = re.compile('^function')


def space_in_func_check(filepath, *args):
    """
        func to check space in js functions
        @str filepath: str path to file what upload from form
    """
    with open('C:/Users/nikin/PycharmProjects/linter/linter/test.js', 'r') as f:
        lines = f.readlines()
        i = 1
        for line in lines:
            if re.search(reg_exp_brace_in_func, line) is not None:
                buf = line.split('(')[1]
                for j in range(1, len(buf) - 1):
                    if buf[j - 1] == ',' and buf[j] != ' ':
                        try:
                            res_len_str['string {}'.format(i)].append('Ошибка в пробелах аргументов функции')
                        except KeyError:
                            res_len_str['string {}'.format(i)] = []
                            res_len_str['string {}'.format(i)].append('Ошибка в пробелах аргументов функции')
            i += 1


def space_in_loop_check(filepath: str, *args):
    """
        func to check space in loop
        @str filepath: str path to file what upload from form
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
        i = 1
        for line in lines:
            if line.find('for') != -1:
                if line[line.find('for'):line.find('for') + 4] != 'for ':
                    try:
                        res_len_str['string {}'.format(i)].append(' Ошибка в пробелах цикла')
                    except KeyError:
                        res_len_str['string {}'.format(i)] = []
                        res_len_str['string {}'.format(i)].append(' Ошибка в пробелах цикла')
            elif line.find('while') != -1:
                if line[line.find('while'):line.find('while') + 6] != 'while ':
                    try:
                        res_len_str['string {}'.format(i)].append(' Ошибка в пробелах цикла')
                    except KeyError:
                        res_len_str['string {}'.format(i)] = []
                        res_len_str['string {}'.format(i)].append(' Ошибка в пробелах цикла')
            i += 1


def space_in_args_check(filepath: str, *args):
    """
        func to check space in args
        @str filepath: str path to file what upload from form
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
        i = 1
        for line in lines:
            if re.search(reg_exp_brace_in_func, line) is not None:
                buffer = line.split("(")[1].split(")")[0]
                for i in range(1, len(buffer)):
                    if buffer[i - 1] == ',' and buffer[i] != ' ':
                        try:
                            res_len_str['string {}'.format(i)].append(' Ошибка в пробелах аргументов')
                        except KeyError:
                            res_len_str['string {}'.format(i)] = []
                            res_len_str['string {}'.format(i)].append(' Ошибка в пробелах аргументов')
            i += 1


def brace_check(filepath: str, *args):
    """
        func to check braces
        @str filepath: str path to file what upload from form
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
        i = 1
        for line in lines:
            if re.search(reg_exp_brace_in_func, line) is not None \
                    and line.split(")") != " {\n":
                try:
                    res_len_str['string {}'.format(i)].append(' Ошибка в скобочках в инициализации функции')
                except KeyError:
                    res_len_str['string {}'.format(i)] = []
                    res_len_str['string {}'.format(i)].append(' Ошибка в скобочках в инициализации функции')
            i += 1


def len_of_string_check(filepath: str):
    """
    func to check len of string
    @str filepath: str path to file what upload from form
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
        i = 1
        for line in lines:
            if len(line) > 120:
                try:
                    res_len_str['string {}'.format(i)].append('Ошибка в длине строки, длина строки больше 120 '
                                                              'символов!')
                except KeyError:
                    res_len_str['string {}'.format(i)] = []
                    res_len_str['string {}'.format(i)].append('Ошибка в длине строки, длина строки больше 120 '
                                                              'символов!')
            i += 1


def main_linter(input_file_path: str) -> dict:
    """
    main point of linter
    @str input_file_path: str path to file what upload from form
    """
    newdoc = Document(docfile=input_file_path)
    newdoc.save()

    len_of_string_check(filepath=newdoc.docfile.name)
    brace_check(filepath=newdoc.docfile.name)
    space_in_args_check(filepath=newdoc.docfile.name)
    space_in_loop_check(filepath=newdoc.docfile.name)
    space_in_func_check(filepath=newdoc.docfile.name)
    print(res_len_str)
    return res_len_str
