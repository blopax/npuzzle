
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


def clean_data(algo_info, data) -> list:
    """
    Clean the data contained in the input file.
    :param dict algo_info: dict containing all the necessary information to run the program
    :param list data: output of the open() function from the file
    :return str: clean_data_int: input data cleaned(cated to int, arranged into lists)
    """
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


def check_first_line(algo_info, data):
    """
    Check the first line of the cleaned data.
    :param dict algo_info: dict containing all the necessary information to run the program
    :param list data: list of int created by the clean_data function
    """
    if len(data) != 1 or data[0] < 2 or type(data[0]) != int:
        algo_info["error"] += "The first line of the file containing the size of the puzzle is not correctly formatted (desired input : single integer (>2) - received input: {0})\n".format(
            data)
        algo_info["board_size"] = 0
    algo_info["board_size"] = data[0]


def check_lenght(algo_info, data):
    """
    Check the format of lines representing the puzzle
    :param dict algo_info: dict containing all the necessary information to run the program
    :param list data: list of list of int representing the values of the puzzle to solve
    """
    size_lst = []
    line_nb = 0
    for each in data:
        size_lst.append(len(each))
        line_nb += 1

    for index, each in enumerate(size_lst):
        if each != algo_info["board_size"]:
            algo_info["error"] += "The width of the puzzle in line {1} does not equal the size of the puzzle (width: {0} // size: {2})\n".format(
                each, index, algo_info["board_size"])

    if line_nb != algo_info["board_size"]:
        algo_info["error"] += "The number of lines of the puzzle does not equal the size of the puzzle (nb_lines: {0} // size: {1})".format(
            line_nb, algo_info["board_size"])


def check_values(algo_info, data):
    """
    Check the values of the lines representing the puzzle
    :param dict algo_info: dict containing all the necessary information to run the program
    :param list data: list of list of int representing the values of the puzzle to solve
    """
    expected_values = [i for i in range(algo_info["board_size"] ** 2)]
    actual_values = []
    for each in data:
        for values in each:
            actual_values.append(values)

    diff = set(expected_values) - set(actual_values)
    if diff:
        algo_info["error"] += "The puzzle does not contain the expected values considering his size {0}. Missing value(s): {1}".format(
            algo_info["board_size"], diff)
    else:
        algo_info["puzzle"] = actual_values


def check_file(algo_info, puzzle_file):
    """
    Check every aspects of the input file
    :param dict algo_info: dict containing all the necessary information to run the program
    :param str pu: list of list of int representing the values of the puzzle to solve
    """
    try:
        with open(puzzle_file, 'r') as f:
            data_puzzle = clean_data(algo_info, f)

        print(data_puzzle)
        if data_puzzle == []:
            raise Exception("EmptyFile")

        check_first_line(algo_info, data_puzzle[0])
        if algo_info["board_size"] < 2:
            algo_info["error"] += "The size cannot be inferior to 2"
        if algo_info["error"] == '':
            check_lenght(algo_info, data_puzzle[1:])
            check_values(algo_info, data_puzzle[1:])

    except IOError:
        algo_info["error"] += "{} cannot be open".format(puzzle_file)
    except UnboundLocalError:
        algo_info["error"] += "Some data is missing"
    except ValueError:
        algo_info["error"] += "The input data contains non-integer values"
    except Exception as e:
        if e.__str__() == "EmptyFile":
            algo_info["error"] += "{0} error: {1} is empty".format(e, puzzle_file)
