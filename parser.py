
import re


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


def clean_data(error, data) -> (str, list):
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

    return error, clean_data_int


def check_first_line(error, data) -> (str, int):
    if len(data) != 1 or data[0] < 2 or type(data[0]) != int:
        error += "The first line of the file containing the size of the puzzle is not correctly formatted (desired input : single integer - received input: {0})\n".format(
            data)
        return error, 0
    return error, data[0]


def check_lenght(error, size, data) -> str:
    size_lst = []
    line_nb = 0
    for each in data:
        size_lst.append(len(each))
        line_nb += 1

    for index, each in enumerate(size_lst):
        if each != size:
            error += "The width of the puzzle in line {1} does not equal the size of the puzzle (width: {0} // size: {2})\n".format(
                each, index, size)

    if line_nb != size:
        error += "The number of line(s) of the puzzle does not equal the size of the puzzle (nb_lines: {0} // size: {1})\n".format(
            line_nb, size)

    return error


def check_values(error, size, data) -> str:
    expected_values = [i for i in range(size ** 2)]
    actual_values = []
    for each in data:
        for values in each:
            actual_values.append(values)

    diff = set(expected_values) - set(actual_values)
    if diff:
        error += "The puzzle does not contain the expected values considering his size {0}\n".format(
            size)
    return error


def check_file(error, puzzle_file) -> str:
    try:
        size = 0
        if puzzle_file == "/dev/random":
            raise Exception("WrongFile")
        with open(puzzle_file, 'r') as f:
            error, data_puzzle = clean_data(error, f)

        print(data_puzzle)
        if data_puzzle == []:
            raise Exception("EmptyFile")

        error, size = check_first_line(error, data_puzzle[0])
        if size < 2:
            error = "The size cannot be inferior to 2\n"
        if error == '':
            error = check_lenght(error, size, data_puzzle[1:])
            error = check_values(error, size, data_puzzle[1:])

    except IOError:
        error = "{} cannot be open\n".format(puzzle_file)
    except FileNotFoundError:
        error = "{} cannot be found\n".format(puzzle_file)
    except UnboundLocalError:
        error = "Some data is missing\n"
    except ValueError:
        error = "The input data contains non-integer values"
    except Exception as e:
        if e.__str__ == "EmptyFile":
            error = "{0} error: {1} is empty\n".format(e, puzzle_file)
        if e.__str__() == "WrongFile":
            print("pouf")
            error = "{0} error: {1} is  not accepted\n".format(e, puzzle_file)
    return error
