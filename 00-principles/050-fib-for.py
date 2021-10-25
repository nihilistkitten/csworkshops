"""Compute the first 8 fibonacci numbers."""

# initial values at (0,1)
prev = 0
curr = 1

# repeat 8 times
for _ in range(8):

    # output the next number
    print(curr)

    # update the numbers according to fibonacci rule: f(n) = f(n-1) + f(n-2)
    # using python's simultaneous assignment notation to allow this
    prev, curr = curr, prev + curr
