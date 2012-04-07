from math import sqrt


def divisors(n):
    d = [i for i in range(2, int(sqrt(n))) if (n % i) == 0]
    d.extend(map(lambda x: n / x, d))
    return d


def primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def rotations(lst):
    return [lst[i:] + lst[0:i] for i in range(len(lst))]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def totient(n):
    return len([i for i in range(1, n) if gcd(i, n) == 1])
