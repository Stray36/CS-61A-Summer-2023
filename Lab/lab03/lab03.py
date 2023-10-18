HW_SOURCE_FILE = __file__


LAB_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(1)
    else:
        return summation(n - 1, term) + term(n)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1:
        return 1
    elif n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    if column == 0:
        return 1
    elif row == 0:
        return 0
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)


def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    last, second_last = n % 10, n // 10 % 10
    if n < 10:
        return False
    elif last == 8 and second_last == 8:
        return True
    else:
        return double_eights(n // 10)
    
    # Alternate solution with helper function: 
    # def helper(num, prev_eight):
    #     if num == 0:
    #         return False
    #     if num % 10 == 8:
    #         if prev_eight:
    #             return True
    #         return helper(num // 10, True)
    #     return helper(num // 10, False)
    # return helper(n, False)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    >>> from construct_check import check
    >>> check(LAB_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    # 不会QAQ
    def interleaved_helper(term0, term1, k):
        if k == n:
            return term0(k)
        return term0(k) + interleaved_helper(term1, term0, k+1)
    return interleaved_helper(odd_term, even_term, 1)

# Alternate solution
def interleaved_sum2(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum2(5, lambda x: x, lambda x: x*x)
    29
    """
    total, term0, term1 = interleaved_helper2(n, odd_term, even_term)
    return total

def interleaved_helper2(n, odd_term, even_term):
    if n == 1:
        return odd_term(1), even_term, odd_term
    else:
        total, term0, term1 = interleaved_helper2(n-1, odd_term, even_term)
        return total + term0(n), term1, term0

# Alternate solution using odd_term and even_term separately
def interleaved_sum3(n, odd_term, even_term):
    def interleaved_helper3(i, fn):
        if i > n:
            return 0
        return fn(i) + interleaved_helper3(i + 2, fn)
    return interleaved_helper3(0, even_term) + interleaved_helper3(1, odd_term)