#!/usr/bin/python3
def safe_print_division(a, b):
    """Prints the division of a by b."""
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
