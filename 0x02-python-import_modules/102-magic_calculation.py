#!/usr/bin/python3
def magic_calculationsa(a, b):
    from magic_calculation_102 import add, sub # type: ignore
    if a < b:
        c = add(a, b)
        for m in range(4, 6):
            c = add(c, m)
            return c
        else:
            return sub(a, b)
        return 0
