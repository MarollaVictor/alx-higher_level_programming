#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opeartor = sys.argv[2]
    if opeartor == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    if opeartor == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if opeartor == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if opeartor == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown opeator. Available opeators: +, -, *, /")
        exit(1)
