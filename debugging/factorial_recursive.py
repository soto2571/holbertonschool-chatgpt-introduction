#!/usr/bin/python3
import sys

def factorial(n):
    """

    Function Description:
    -----------------------
    This function calculates the factorial of a given integer 'n' using recursion.
    The factorial of a non-negative integer 'n' is the product of all positvie integers less than ot equal to 'n'.

    Parameters:
    -----------
    n : int
        The integer for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the given integer 'n'.
        """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
