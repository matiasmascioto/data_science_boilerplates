"""
Helper functions
"""

from functools import wraps
from time import time


def timing(f):
    """Decorator for timing functions
    Usage:
    @timing
    def function(a):
        pass
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f"Function: {f.__name__} - Execution time: {end - start:.2f} seconds")
        return result

    return wrapper
