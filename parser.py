
import re


def check_first_line(error, data) -> (bool, int):
    print(data)
    if len(data) != 1 and data < 2:
        print(data[0])
        error = True

    return error, data[0]


def check_lenght(error, size, data) -> int:
    size_lst = []
    line_nb = 0
    for each in data:
        size_lst.append(len(each))
        line_nb += 1

    for each in size_lst:
        print("each : {0}, size : {1}".format(each, size))
        if each != size:
            error = True
    print(error)
    if line_nb != size:
        error = True
    print(error)
    
    print("OK, {} elements dans chaque lignes".format(size))
    return error


def strip_comment(line):
    """
    Clean lines that have comments.
    :param str line: line: full line
    :return str: cleaned_line: line without comments
    """
    if "#" in line:
        line_split = line.split('#')
        line = line_split[0]

    return line.strip()


def clean_data(data) -> list:
    raw = data.read()
    newline_split = raw.split('\n')
    uncommented = []

    for line in newline_split:
        uncommented.append(strip_comment(line))

    no_empty_strings = list(filter(None, uncommented))
    no_double_spaces = [' '.join(each.split()) for each in no_empty_strings]

    clean_data = [each.split(' ') for each in no_double_spaces]
    clean_data_int = []
    for each in clean_data:
        clean_data_int.append([int(numbers) for numbers in each])

    return clean_data_int


def check_file(puzzle_file) -> bool:
    error = False
    with open(puzzle_file, 'r') as f:
        data_puzzle = clean_data(f)

    print(data_puzzle)
    error, size = check_first_line(error, data_puzzle[0])
    print(error)
    error = check_lenght(error, size, data_puzzle[1:])
    return True
