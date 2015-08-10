#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        input = raw_input("Enter an integer: ")
    except:
        print ("Tut, tut. That's not a number.")
    else:
        input = int(input)
        if input%2 == 0:
            print "That's an even integer, I can tell."
        else:
            print "Looks like an odd integer to me."


def ten_by_ten():
    row = ""
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for x in range(1,101):
        row = row + str(x).rjust(3-len(str(x))) + " "
        if x%10 == 0:
            print row
            #Reset row
            row = ""


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    num_list = []
    while True:
        input = raw_input("Enter a number: ")
        if input == 'done':
            average = float(sum(num_list))/len(num_list)
            return average
        else:
            try:
                number = int(input)
            except:
                print("That's not a number.")
            else:
                num_list.append(number)

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    #even_odd()
    ten_by_ten()
    #print find_average()

if __name__ == '__main__':
    main()
