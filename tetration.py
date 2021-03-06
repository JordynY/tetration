# This program calculates y = x|k,
# Warning:
# There is no timeout so be careful what you pass it

import argparse
from varname import nameof


def find_k(y, x):  # as yet not finished so don't use
    print("Not implemented, Don't use")
    return None


def calc_x(y, k):  # calculates x given y and k, linear search up from 1 to 5 and from -1 to -5
    found = False
    for x in range(1, 6):
        if y == calc_y(x, k):
            out = x
            found = True
            break
        elif y == calc_y(x * -1, k):
            out = x * -1
            found = True
            break
    if found:
        return x
    else:
        return None


def calc_y(x, k):  # calculate y = x|k
    y = 1
    if k < 0 or x == 0:
        raise ValueError("x or k value not allowed")
    elif k > 0:
        y = x ** calc_y(x, k - 1)
    return y


def console_converter(default, name, needed):
    if needed:  # get value from user, assuming it hasn't already been given
        assign = int(input("Please enter " + name + ": "))
        return assign
    else:  # if user has already provided value in command line
        return default


def calc(p, q):
    return calc_y(p, q)  # used to set calc() to default to calc_y()


def main():
    # parse all command line variables
    parser = argparse.ArgumentParser()
    parser.add_argument("num1", type=int, nargs='?', const=0)
    parser.add_argument("num2", type=int, nargs='?', const=0)
    parser.add_argument('-x', '--calculate_x', action='store_true', help="allows finding of x")
    parser.add_argument('-y', '--calculate_y', action='store_true', help="allows finding of x")
    args = parser.parse_args()

    # find out if variables are needed from the user, its all or nothing btw
    needed = args.num2 is None

    # get option from user if needed
    m = console_converter(0, "\n0 to calculate y given x & k\n1 to calculate x given y & k\n", needed)

    # calculate various values give options, getting user input if needed
    if args.calculate_x or m == 1:  # if option = 1
        out = calc_x(console_converter(args.num1, "y", needed), console_converter(args.num2, "k", needed))
    elif args.calculate_y or m == 0:  # if option = 0
        out = calc_y(console_converter(args.num1, "x", needed), console_converter(args.num2, "k", needed))
    else:  # defaults to option = 0, included twice for completeness
        out = calc(console_converter(args.num1, "x", needed), console_converter(args.num2, "k", needed))

    # print the answer
    print(out)


if __name__ == "__main__":
    main()
