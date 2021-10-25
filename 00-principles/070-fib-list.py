"""Compute the first 8 fibonacci numbers."""


def fib_step(prev, curr):
    """Return the new previous and current numbers according to the fibonacci rule."""
    # return (f(n-1), f(n-1) + f(n-2))
    return curr, prev + curr


def first_n_fib(n):
    """Return a list of the first n fibonacci numbers."""
    # initial values at (0,1)
    prev = 0
    curr = 1

    # stores the computed values for later return
    ret = []

    # repeat n times
    for _ in range(n):

        # store the next number
        ret.append(curr)

        # update the numbers
        prev, curr = fib_step(prev, curr)

    return ret


def print_list(to_print):
    """Print each value in to_print."""
    for val in to_print:
        print(val)


lst = first_n_fib(8)
print_list(lst)
