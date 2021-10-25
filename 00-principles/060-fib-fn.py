"""Compute the first 8 fibonacci numbers."""


def fib_step(prev, curr):
    """Return the new previous and current numbers according to the fibonacci rule."""
    # return (f(n-1), f(n-1) + f(n-2))
    return curr, prev + curr


def print_first_n_fib(n):
    """Print the first n fibonacci numbers."""
    # initial values at (0,1)
    prev = 0
    curr = 1

    # repeat n times
    for _ in range(n):

        # output the next number
        print(curr)

        # update the numbers
        prev, curr = fib_step(prev, curr)


print_first_n_fib(8)
