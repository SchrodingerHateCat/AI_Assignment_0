""" File name:   truth_tables.py
    Author:      <Zhengduo Zhu>
    Date:        <01/03/2021>
    Description: This file defines a number of functions which implement Boolean
                 expressions.

                 It also defines a function to generate and print truth tables
                 using these functions.

                 It should be implemented for Exercise 2 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""


def boolean_fn1(a, b, c):
    """ Return the truth value of (a ∨ b) → (-a ∧ -b) """
    # YOUR CODE HERE
    return (not (a or b)) or ((not a) and (not b))


def boolean_fn2(a, b, c):
    """ Return the truth value of (a ∧ b) ∨ (-a ∧ -b) """
    # YOUR CODE HERE
    return (a and b) or ((not a) and (not b))


def boolean_fn3(a, b, c):
    """ Return the truth value of ((c → a) ∧ (a ∧ -b)) ∨ (-a ∧ b) """
    # YOUR CODE HERE
    return (((not c) or a) and (a and (not b))) or ((not a) and b)


def draw_truth_table(boolean_fn):
    """ This function prints a truth table for the given boolean function.
        It is assumed that the supplied function has three arguments.

        ((bool, bool, bool) -> bool) -> None

        If your function is working correctly, your console output should look
        like this:

        >>> from truth_tables import *
        >>> draw_truth_table(boolean_fn1)
        a     b     c     res
        -----------------------
        False False False True
        False False True  True
        False True  False False
        False True  True  False
        True  False False False
        True  False True  False
        True  True  False False
        True  True  True  False
    """
    # YOUR CODE HERE
    print ("a     b     c     res")
    print ("-----------------------")
    print ("False False False "+str(boolean_fn(0,0,0)))
    print ("False False True  "+str(boolean_fn(0,0,1)))
    print ("False True  False "+str(boolean_fn(0,1,0)))
    print ("False True  True  "+str(boolean_fn(0,1,1)))
    print ("True  False False "+str(boolean_fn(1,0,0)))
    print ("True  False True  "+str(boolean_fn(1,0,1)))
    print ("True  True  False "+str(boolean_fn(1,1,0)))
    print ("True  True  True  "+str(boolean_fn(1,1,1)))

