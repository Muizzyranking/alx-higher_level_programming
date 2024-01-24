#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format().
    Args:
        value (int): The integer to print.
    Returns:
        If value is a string - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
