#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    no_of_elements = 0

    for elements in range(x):
        try:
            print("{}".format(my_list[elements]), end="")
            no_of_elements += 1
        except IndexError:
            break
    print("")
    return no_of_elements
