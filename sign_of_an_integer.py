#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program checks the sign of an integer inputted by the user


def main():
    # this function determines the sign of the inputted integer

    # input
    number = int(input("Enter an integer: "))

    # process & output
    if number > 0:
        print("\nThis integer is positive.")
    elif number < 0:
        print("\nThis integer is negative.")
    else:
        print("\nThis number is 0.")
    print("\nDone.")


if __name__ == "__main__":
    main()
