prev = 0
curr = 1

count = 0
while count < 8:
    print(curr)
    prev, curr = curr, prev + curr
    count += 1
