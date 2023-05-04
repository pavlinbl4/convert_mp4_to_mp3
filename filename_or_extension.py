import re


def select_file_name(file_name):
    pattern = r'.+(?=\.)'
    return re.search(pattern, file_name).group()


def select_file_extension(file_name):
    pattern = r'(?<=\.).+'
    return re.search(pattern, file_name).group()


def list_string_way(file_name):
    return file_name.split('.')


if __name__ == '__main__':
    print(select_file_name("2022_avgust.xls"))
    print(select_file_extension("2022_avgust.xls"))
    print(list_string_way("2022_avgust.xls"))
