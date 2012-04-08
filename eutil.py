from math import sqrt, ceil


def take(iterable, n):
    "Return first n items of the iterable as a list"
    from itertools import islice

    return list(islice(iterable, n))


def divisors(n, small=False):
    d = [x for x in range(1, int(ceil(sqrt(n))) + 1) if (n % x) == 0]
    if not small:
        d.extend(map(lambda x: n / x, d))
    return list(set(d))


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


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


def triangle_numbers():
    from itertools import count, imap

    return imap(lambda n: n * (n + 1) / 2, count(start=1))


def rotations(lst):
    return [lst[i:] + lst[0:i] for i in range(len(lst))]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) / gcd(a, b)


def totient(n):
    return len([i for i in range(1, n) if gcd(i, n) == 1])
