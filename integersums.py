# integersums.py
""" Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""
def first(n):
    num = 1
    sum = 0
    while num < n + 1:
        sum = sum + num
        num = num + 1
    return sum