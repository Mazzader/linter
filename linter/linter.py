import re

res_len_str = {}
res = {}
reg_exp_brace_in_func = re.compile('^function [.]+\([.]+\)$')


def space_in_func_check(upload_files, *args):
    pass


def space_in_loop_check(upload_files, *args):
    for i in range(len(upload_files)):
        for string in upload_files[i]:
            if string.find('for'):
                if string[string.find('for'):string.find('for') + 4] != 'for ':
                    res_len_str[upload_files[i]] = string


def space_in_args_check(upload_files, *args):
    for i in range(len(upload_files)):
        for string in upload_files[i]:
            if re.search(reg_exp_brace_in_func, string) is not None:
                buffer = string.split("(")[1].split(")")[0]
                for i in range(1, len(buffer)):
                    if buffer[i - 1] == ',' and buffer[i] != ' ':
                        res_len_str[upload_files[i]] = string


def sintyx_in_func_code(upload_files, *args):
    pass


def brace_check(upload_files, *args):
    for i in range(len(upload_files)):
        for string in upload_files[i]:
            if re.search(reg_exp_brace_in_func, string) is not None \
                    and string.split(")") != " {\n":
                res_len_str[upload_files[i]] = string


def len_of_string_check(upload_files, *args):
    for i in range(len(upload_files)):
        for string in upload_files[i]:
            if len(string) > 120:
                res_len_str[upload_files[i]] = string


def handle_uploaded_file(f, uu_id):
    print(f)
    with open('{}.txt'.format(uu_id), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def linter_handler(f):
    len_of_string_check(f)
    brace_check(f)
    space_in_args_check(f)
    space_in_loop_check(f)
    space_in_func_check(f)
    return res_len_str
