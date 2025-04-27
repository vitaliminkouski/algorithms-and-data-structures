
MOD = 1000000007
len_of_row, num_of_ones = map(int, input().split())


def factorial(n):
    if(n==0):
        return 1
    for i in range(1, n):
        n = (n * i) % MOD
    return n


def bin_pow(a, n):
    a %= MOD
    if (n == 0):
        return 1
    if (n == 1):
        return a
    t = bin_pow(a, n >> 1)
    if ((n & 1) == 0):
        return (t * t) % MOD
    return (((t * t) % MOD) * a) % MOD


result = (factorial(len_of_row) * bin_pow(factorial(num_of_ones), MOD - 2)) % MOD
result = (result * bin_pow(factorial(len_of_row - num_of_ones), MOD - 2)) % MOD

print(result)
