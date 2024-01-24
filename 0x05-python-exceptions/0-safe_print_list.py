#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints the x element of a my_list
    Args:
        my_list: list
        x: int
    Return:
        count: int
    """
    count = 0
    try:
        for i in my_list[:x]:
            print(f"{i}", end="")
            count += 1
    except IndexError:
        pass

    print()
    return count
