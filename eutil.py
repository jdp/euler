from math import sqrt, ceil
from functools import partial


class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return partial(self.__call__, obj)


def take(n, iterable):
    "Return first n items of the iterable as a list"
    from itertools import islice

    return list(islice(iterable, n))


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    from itertools import islice

    return next(islice(iterable, n, None), default)


def iterate(func, x):
    while True:
        yield func(x)
        x = func(x)


def digits(n):
    return map(int, list(str(n)))


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


@memoized
def is_prime(n):
    for p in primes():
        if p == n:
            return True
        if p > n:
            return False


def sequence(func, start=0):
    from itertools import count, imap

    return imap(func, count(start=start))


def triangle_numbers(start=1):
    return sequence(lambda n: n * (n + 1) / 2, start=1)


def rotations(lst):
    return [lst[i:] + lst[0:i] for i in range(len(lst))]


def ilen(iterable):
    return sum(1 for _ in iterable)


@memoized
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


@memoized
def lcm(a, b):
    return (a * b) / gcd(a, b)


@memoized
def totient(n):
    return len([i for i in range(1, n) if gcd(i, n) == 1])
