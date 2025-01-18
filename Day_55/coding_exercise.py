# Advanced Decorators
# Create a logging_decorator() which is going to print the name of the function that was called,
# the arguments it was given and finally the returned output:
# You called a_function(1,2,3)
# It returned: 6
# The value 6 is the return value of the function.
# Don't change the body of a_function.
# IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.

# TODO: Create the logging_decorator() function 👇
from functools import wraps


def logging_decorator(function):
    @wraps(function)
    def wrapper(*args):
        value: int = function(*args)
        print(f'You called {function.__name__}{args}\n'
              f'It returned: {value}')
        return value
    return wrapper

# TODO: Use the decorator 👇


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
