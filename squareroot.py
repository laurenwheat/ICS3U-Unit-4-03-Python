#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program determines the square of a number

def main():

    loop_counter = 1
    square_num = 1

    user_input = input("Enter a positive integer: ")
    print("")

    try:

        user_input_int = int(user_input)

        if user_input_int >= 0:
            for loop_counter in range(user_input_int + 1):
                square_num = loop_counter**2
                print("{0}² = {1}".format(loop_counter, square_num))
    except Exception:
        print("That is not a positive integer!!!!!")
    finally:
        print("")
        print("Thanks for playing!!")


if __name__ == "__main__":
    main()
