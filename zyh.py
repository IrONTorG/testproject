def sum_fib(n):
    c = 1
    p = 0
    s = 0
    while c < n:
        s += c
        c, p = c + p, c
    return s


print(sum_fib(5))