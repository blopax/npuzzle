
import math
import copy

def fill_right(n, sorted_list, x, y, i):
    """
    Fill the number from left to right until it reachs the border or an already filled slot, update i, x, y values"
    :param int n: size of puzzle
    :param list sorted_list: list with the position of each value in the good spot
    :param int i: current value to be added int the list
    :param int x: x coordinate in the puzzle
    :param int y: y coordinate in the puzzle
    :return list: list of size n^2 with the solution
    """

    #print("RIGHT START")
    if sorted_list[(n*y) + x] != None:
        x+= 1

    while x < n - 1 and sorted_list[(n*y) + x] == None and i < n**2:
        #print("RIGHT WHILE IN")
        sorted_list[(n*y) + x] = i
        i += 1
        if sorted_list[(n*y) + x + 1] == None:
            x += 1
    #print("RIGHT END")
    return sorted_list, x, y, i

def fill_down(n, sorted_list, x, y, i):
    """
    Fill the number from up to down until it reachs the border or an already filled slot, update i, x, y values"
    :param int n: size of puzzle
    :param list sorted_list: list with the position of each value in the good spot
    :param int i: current value to be added int the list
    :param int x: x coordinate in the puzzle
    :param int y: y coordinate in the puzzle
    :return list: list of size n^2 with the solution
    """
    #print("DOWN START")
    print("x = {0} y = {1} i = {2}".format(x,y,i))
    if sorted_list[(n*y) + x] != None:
        y+= 1
        
    while y < n - 1 and sorted_list[(n*y) + x] == None and i < n**2:
        #print("x = {0} y = {1} i = {2} - (n*y) + x = {3}".format(x,y,i,(n*y + x)))
        #print("DOWN WHILE IN")
        sorted_list[(n*y) + x] = i
        i += 1
        if sorted_list[(n*(y+1)) + x] == None:
            y += 1
    #print("DOWN END")
    return sorted_list, x, y, i

def fill_left(n, sorted_list, x, y, i):
    """
    Fill the number from right to left until it reachs the border or an already filled slot, update i, x, y values"
    :param int n: size of puzzle
    :param list sorted_list: list with the position of each value in the good spot
    :param int i: current value to be added int the list
    :param int x: x coordinate in the puzzle
    :param int y: y coordinate in the puzzle
    :return list: list of size n^2 with the solution
    """
    if sorted_list[(n*y) + x] != None and x > 0:
        x-= 1
        
    while x >= 0 and sorted_list[(n*y) + x] == None and i < n**2:
        sorted_list[(n*y) + x] = i
        i += 1
        if x > 0 and sorted_list[(n*y) + x - 1] == None:
            x -= 1
    return sorted_list, x, y, i

def fill_up(n, sorted_list, x, y, i):
    """
    Fill the number from down to up until it reachs the border or an already filled slot, update i, x, y values"
    :param int n: size of puzzle
    :param list sorted_list: list with the position of each value in the good spot
    :param int i: current value to be added int the list
    :param int x: x coordinate in the puzzle
    :param int y: y coordinate in the puzzle
    :return list: list of size n^2 with the solution
    """
    if sorted_list[(n*y) + x] != None:
        y-= 1
        
    while y > 0 and sorted_list[(n*y) + x] == None and i < n**2:
        sorted_list[(n*y) + x] = i
        i += 1
        if y > 1 and sorted_list[(n*(y-1)) + x] == None:
            y -= 1
    return sorted_list, x, y, i

def create_goal(n) ->list:
    """
    Returns as a list the goal to reach for a n-puzzle of size n in a snail style"
    :param int n: size of puzzle
    :return list: list of size n^2 with the solution
    """

    sorted_list = [None] * (n**2)
    i = 1
    x = 0
    y = 0

    while i < n**2:

        if i < n**2:
            sorted_list, x, y, i = fill_right(n, sorted_list, x, y, i)
            print("x = {0} y = {1} i = {2}".format(x,y,i))
        if i < n**2:
            sorted_list, x, y, i = fill_down(n, sorted_list, x, y, i)
            print("x = {0} y = {1} i = {2}".format(x,y,i))
        if i < n**2:
            sorted_list, x, y, i = fill_left(n, sorted_list, x, y, i)
            print("x = {0} y = {1} i = {2}".format(x,y,i))
        if i < n**2:
            sorted_list, x, y, i = fill_up(n, sorted_list, x, y, i)
            print("x = {0} y = {1} i = {2}".format(x,y,i))

    k = 0
    while sorted_list[k] != None:
        k += 1
    sorted_list[k] = 0

    print(sorted_list)


def action(puzzle, tile) ->list:
    """
    Returns the state of the puzzle after swapping tile. Returns error if tile can not be swapped.
    :param list puzzle:
    :param int tile:
    :return list:
    """

    try:
        for index, item in enumerate(puzzle):
            if item == 0:
                index_zero = index
            if item == tile:
                index_tile = index

        size = math.sqrt(len(puzzle))
        x_tile = index_tile % size
        y_tile = index_tile // size
        x_zero = index_zero % size
        y_zero = index_zero // size

        vertical_swap = (x_tile == x_zero and math.fabs(y_tile - y_zero) == 1)
        horizontal_swap = (y_tile == y_zero and math.fabs(x_tile - x_zero) == 1)
        if not (horizontal_swap or vertical_swap):
            raise Exception("No swap possible")

        new_state_puzzle = copy.deepcopy(puzzle)
        new_state_puzzle[int(y_tile * size + x_tile)] = 0
        new_state_puzzle[int(y_zero * size + x_zero)] = tile
        return new_state_puzzle
    except Exception as e:
        print(e)

    #should probably create class Tile with value, index, x, y


def print_puzzle(puzzle) ->None:
    """

    :param list puzzle:
    :return: void function
    """


if __name__ == "__main__":
    P = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(P)
    Q = action(P, 1)
    print(Q)
    Q = action(P, 2)
    print(Q)
    Q = action(P, 3)
    print(Q)
    Q = action(P, 4)
    print(Q)
    Q = action(P, 5)
    print(Q)
    Q = action(P, 6)
    print(Q)
    Q = action(P, 7)
    print(Q)
    Q = action(P, 8)
    print(Q)

if __name__ == "__main__":
    create_goal(3)
    create_goal(4)
    create_goal(5)
    #create_goal(10)
    #create_goal(50)