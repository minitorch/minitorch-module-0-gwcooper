"""Collection of the core mathematical operators used throughout the code base."""

import math
from typing import Callable, Iterable, Union

# ## Task 0.1

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(a, b):
    """Multiply two numbers."""
    return a * b


def id(i):
    """Return the input unchanged."""
    return i


def add(a, b):
    """Return the sum."""
    return a + b


def neg(i):
    """Negate the input."""
    return -i


def lt(a, b):
    """Check if a < b."""
    return a < b


def eq(a, b):
    """Check if a == b."""
    return a == b


def max(a, b):
    """Return the larger input value."""
    if a >= b:
        return a
    return b


def is_close(a, b):
    """Check if two numbers are close in value."""
    # $f(x) = |x - y| < 1e-2$
    delta = 1e-2
    return abs(a - b) < delta


def sigmoid(x):
    """Calculate the value of a sigmoid function for a given input x."""
    if x <= 0:
        return math.exp(x) / (1.0 + math.exp(x))
    return 1.0 / (1.0 + math.exp(-x))


def relu(x):
    """Calculate the output of the relu function for a given input x."""
    if x <= 0:
        return 0
    return x


def log(x):
    """Calculate the natural logarithm of the input x."""
    return math.log(x)


def exp(x):
    """Calculate the exponential function output for the input x."""
    return math.exp(x)


def inv(x):
    """Calculate the reciprocal of the input x."""
    return 1 / x


def inv_back(x, y):
    """Compute the derivative of the reciprocal of x multiplied by y."""
    # I think this means the derivative of inv(x) * y?
    # 1 / x * y = y / x - how to get the derivative of values?
    return y / inv(x)


def relu_back(x, y):
    """Compute the derivative of ReLU multiplied by y."""
    return (x > 0) * y


def log_back(x, y):
    """Compute the derivative of log(x) multiplied by y."""
    return (1 / x) * y


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.


def map(x: Callable, iterable: Iterable):
    """Apply the function x to a given iterable."""
    return [x(i) for i in iterable]


def zipWith(x: Callable, iter1: Iterable, iter2: Iterable):
    """Combine the elements of iter1 and iter2 via the function x."""
    return [x(i, j) for i, j in zip(iter1, iter2)]


def reduce(x: Callable, iterable: list):
    """Reduce the values in an iterable using a given function x."""
    if len(iterable):
        prev = iterable[0]
        for i in iterable[1:]:
            prev = x(prev, i)
        return prev
    return 0


def negList(input_list: list):
    """Negate a given list."""
    return map(neg, input_list)


def addLists(list1: list, list2: list):
    """Add two lists."""
    return zipWith(add, list1, list2)


def sum(input_list: list) -> Union[int, float]:
    """Sum the values in a list."""
    return reduce(add, input_list)


def prod(input_list: list) -> Union[int, float]:
    """Calculate the product of values in a list."""
    return reduce(mul, input_list)
