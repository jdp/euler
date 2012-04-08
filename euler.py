# -*- coding: utf-8 -*-

import argparse
import sys


def euler_1():
    """Add all the natural numbers below one thousand that are multiples of 3 or 5."""
    return sum([n for n in range(1000) if n % 3 == 0 or n % 5 == 0])


def euler_2():
    """By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""
    from itertools import takewhile
    from eutil import fib

    return sum(filter(lambda x: x % 2 == 0, takewhile(lambda y: y < 4000000, fib())))


def euler_3():
    """Find the largest prime factor of a composite number."""
    from math import sqrt
    from itertools import takewhile
    from eutil import primes

    num = 600851475143
    ps = takewhile(lambda p: p < sqrt(num), primes())
    return max([p for p in ps if num % p == 0])


def euler_4():
    """Find the largest palindrome made from the product of two 3-digit numbers."""
    palindromes = [i * j for i in range(999, 100, -1) for j in range(990, 100, -11) if str(i * j) == str(i * j)[::-1]]
    return max(palindromes)


def euler_5():
    """What is the smallest number divisible by each of the numbers 1 to 20?"""
    from eutil import lcm
    return reduce(lambda x, y: lcm(x, y), range(1, 21), 1)


def euler_6():
    """What is the difference between the sum of the squares and the square of the sums?"""
    n = 100
    sum_of_squares = sum(map(lambda x: x ** 2, range(1, n + 1)))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return abs(sum_of_squares - square_of_sum)


def euler_7():
    """Find the 10001st prime."""
    from eutil import primes, nth

    return nth(primes(), 10000)


def euler_8():
    """Discover the largest product of five consecutive digits in the 1000-digit number."""
    from operator import __mul__

    n = ''.join([line.strip() for line in open("data/8.txt")])
    return max([reduce(__mul__, map(int, list(n[i:i + 5]))) for i in range(len(n) - 5)])


def euler_9():
    """Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000."""
    from math import floor

    for b in range(1, 1001):
        a = (500000.0 - 1000 * b) / (1000 - b)
        if floor(a) == a:
            c = 1000 - a - b
            return int(a * b * c)


def euler_10():
    """Calculate the sum of all the primes below two million."""
    from itertools import takewhile
    from eutil import primes

    return sum(takewhile(lambda p: p < 2000000, primes()))


def euler_12():
    """What is the value of the first triangle number to have over five hundred divisors?"""
    from itertools import dropwhile
    from eutil import triangle_numbers, divisors

    return next(dropwhile(lambda x: len(divisors(x)) < 500, triangle_numbers()))


def euler_13():
    """Find the first ten digits of the sum of one-hundred 50-digit numbers."""
    numbers = [int(line) for line in open("data/13.txt")]
    return str(sum(numbers))[:10]


# TODO: functional style
def euler_14():
    """Find the longest sequence using a starting number under one million."""
    lengths = {}

    def sequence(n):
        m = n
        length = 1
        while m != 1:
            if m in lengths:
                length += lengths[m]
                break
            if m % 2 == 0:
                m = m / 2
            else:
                m = 3 * m + 1
            length += 1
        lengths[n] = length
        return length

    max_length, max_n = 0, 1
    for n in range(1, 1000000):
        length = sequence(n)
        if length > max_length:
            max_length = length
            max_n = n
    return max_n


def euler_18():
    """Find the maximum sum travelling from the top of the triangle to the base."""
    triangle = [map(int, line.split()) for line in open("data/18.txt")]

    def max_row_sums(above, below):
        r = [0] + above + [0]
        return map(lambda t: max(t[1] + r[t[0]], t[1] + r[t[0] + 1]), enumerate(below))

    return max(reduce(max_row_sums, triangle))


def euler_21():
    """Evaluate the sum of all amicable pairs under 10000."""
    from eutil import divisors

    def d(n):
        return sum(sorted(divisors(n))[:-1])

    return sum([a for a in range(1, 10000) if a != d(a) and d(d(a)) == a])


def euler_22():
    """What is the total of all the name scores in the file of first names?"""
    names = sorted(map(lambda w: w.strip('"'), open("data/22.txt").read().split(",")))
    return sum([(i * sum([(ord(c) - 64) for c in name])) for i, name in enumerate(names, 1)])


def euler_23():
    """Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
    from eutil import divisors

    abundants = set([n for n in range(1, 20162) if sum(sorted(divisors(n))[:-1]) > n])
    return sum(n for n in range(1, 20162) if not any(((n - a) in abundants) for a in abundants))


def euler_24():
    """What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
    from itertools import permutations
    from eutil import nth

    return "".join(map(str, nth(permutations(range(10), 10), 999999)))


def euler_25():
    """What is the first term in the Fibonacci sequence to contain 1000 digits?"""
    from itertools import takewhile
    from eutil import fib

    return len(list(takewhile(lambda x: len(str(x)) < 1000, fib())))


def euler_29():
    """How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?"""
    m = 101
    return len(set([a ** b for a in range(2, m) for b in range(2, m)]))


def euler_35():
    """How many circular primes are there below one million?"""
    from operator import __and__
    from itertools import takewhile
    from eutil import primes, rotations

    circular = 0
    max_n = 1000000
    ps = set(takewhile(lambda p: p < max_n, primes()))
    for p in ps:
        rotate_perms = [int("".join(r)) for r in rotations(list(str(p)))]
        if reduce(__and__, [(x in ps) for x in rotate_perms]):
            circular += 1
    return circular


def euler_63():
    """How many n-digit positive integers exist which are also an nth power?"""
    from math import log10

    return sum([int(1 / (1 - log10(n))) for n in range(1, 10)])


def euler_67():
    """Using an efficient algorithm find the maximal sum in the triangle?"""
    triangle = [([0] + map(int, line.split()) + [0]) for line in open("data/67.txt")]

    def max_row_sums(above, below):
        return [0] + [(max(t[1] + above[t[0]], t[1] + above[t[0]+1])) for t in enumerate(below[1:-1])] + [0]

    return max(reduce(max_row_sums, triangle))


def euler_69():
    """Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum."""
    from eutil import primes

    n = 1
    for p in primes():
        if (n * p) > 1000000:
            break
        n = n * p
    return n


def euler_92():
    """Investigating a square digits number chain with a surprising property."""
    from itertools import dropwhile
    from math import factorial
    from operator import mul
    from eutil import iterate, digits

    def sum_sq_digits(n):
        return sum([x ** 2 for x in digits(n)])

    # TODO: Make this generic, and not totally ugly
    def combos():
        for a in range(10):
            for b in range(a + 1):
                for c in range(b + 1):
                    for d in range(c + 1):
                        for e in range(d + 1):
                            for f in range(e + 1):
                                for g in range(f + 1):
                                    yield a + (b * 10) + (c * 100) + (d * 1000) + (e * 10000) + (f * 100000) + (g * 1000000)

    def multinomial(n):
        alphabet = dict([(d, digits(n).count(d)) for d in set(digits(n))])
        alphabet[0] = 7 - len(str(n))
        return factorial(sum(alphabet.values())) / reduce(mul, map(factorial, alphabet.values()))

    unhappy = set(i for i in range(1, 568) if 89 == next(dropwhile(lambda x: x != 1 and x != 89, iterate(sum_sq_digits, i))))
    return sum([multinomial(i) for i in combos() if sum_sq_digits(i) in unhappy])


if __name__ == '__main__':
    def print_solution(id, func):
        from inspect import cleandoc

        print "-- Problem", id
        print cleandoc(func.__doc__)
        print func()
        print

    def solved_problems():
        problems = [(name, int(name[6:])) for name in globals().keys() if name[:5] == 'euler']
        return sorted(problems, key=lambda p: p[1])

    parser = argparse.ArgumentParser(description="Run Project Euler solutions")
    parser.add_argument('--summary', action='store_true')
    parser.add_argument('--problems', '-p', nargs='*', type=int)
    args = parser.parse_args()

    if args.summary:
        problem_nos = map(lambda p: p[1], solved_problems())
        print len(problem_nos), "problems are solved:", ", ".join(map(str, problem_nos))
    elif isinstance(args.problems, list):
        for problem in args.problems:
            name = 'euler_' + str(problem)
            if name in globals():
                print_solution(int(problem), globals()[name])
            else:
                print problem, "is not yet solved!"
                sys.exit(1)
    else:
        for problem in solved_problems():
            print_solution(problem[1], globals()[problem[0]])
