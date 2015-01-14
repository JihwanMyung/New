"""
sum_n(n)
--
exercise function
"""


def sum_n(n):
    """
    sums n in the range(n) and returns the result
    """
    total = 0
    for i in range(1,n+1):
        total += i
    
    return total
