import re

res_len_str = {}
res = {}
reg_exp_brace_in_func = re.compile('^function')


def space_in_func_check(*args):
    pass


def space_in_loop_check(*args):
    #TODO дописать эту хуйню дома!
    with open('test.js', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.find('for') != -1:
                if line[line.find('for'):line.find('for') + 4] != 'for ':
                    try:
                        res_len_str[line].append(' Ошибка в пробелах цикла ')
                    except KeyError:
                        res_len_str[line] = []
                        res_len_str[line].append(' Ошибка в пробелах цикла')


def space_in_args_check(*args):
    with open('test.js', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(reg_exp_brace_in_func, line) is not None:
                buffer = line.split("(")[1].split(")")[0]
                for i in range(1, len(buffer)):
                    if buffer[i - 1] == ',' and buffer[i] != ' ':
                        try:
                            res_len_str[line].append(' Ошибка в пробелах ')
                        except KeyError:
                            res_len_str[line] = []
                            res_len_str[line].append(' Ошибка в пробелах ')


def sintyx_in_func_code(upload_files, *args):
    pass


def brace_check(*args):
    with open('test.js', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(reg_exp_brace_in_func, line) is not None \
                    and line.split(")") != " {\n":
                try:
                    res_len_str[line].append(' Ошибка в скобочках) ')
                except KeyError:
                    res_len_str[line] = []
                    res_len_str[line].append(' Ошибка в скобочках) ')



def len_of_string_check(*args):
    with open('test.js', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) > 120:
                try:
                    res_len_str[line].append(' Ошибка в длине строки, длина строки больше 120 символов!')
                except KeyError:
                    res_len_str[line] = []
                    res_len_str[line].append(' Ошибка в длине строки, длина строки больше 120 символов!')


len_of_string_check()
brace_check()
space_in_args_check()
space_in_loop_check()
print(res_len_str)