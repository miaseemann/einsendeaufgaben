def f(n, k):
    if k == 0 or k == n:
        return 1
    return (n * f(n - 1, k - 1)) // k

print(f(49, 6))
