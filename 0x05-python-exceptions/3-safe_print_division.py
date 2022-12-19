#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
Footer
© 2022 GitHub, Inc.
Footer navigation
Term
