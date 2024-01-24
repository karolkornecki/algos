from sys import setrecursionlimit

# stable string sorting algorithm of variable length
# complexity: linear

# extended ASCII
R = 256

setrecursionlimit(100000)


def msd_sort(a: [str]):
    n = len(a)
    aux = [None for _ in range(n)]
    sort(a, 0, n - 1, 0, aux)


def sort(a, lo, hi, d, aux):
    if hi <= lo:
        return

    # frequency count
    count = [0 for _ in range(R + 2)]
    for i in range(lo, hi + 1):
        c = char_at(a[i], d)
        count[id(c) + 2] += 1

    # compute cumulates
    for r in range(R + 1):
        count[r + 1] += count[r]

    # distribute
    for i in range(lo, hi + 1):
        c = char_at(a[i], d)
        aux[count[id(c) + 1]] = a[i]
        count[id(c) + 1] += 1

    # copy back
    for i in range(lo, hi + 1):
        a[i] = aux[i - lo]

    # recursively sort for each character (excludes sentinel -1)
    for r in range(R):
        sort(a, lo + count[r], lo + count[r + 1] - 1, d + 1, aux)


def id(s):
    """ Return ASCII int of character or int"""
    if isinstance(s, int):
        return s
    return ord(s)


def char_at(s, d):
    if len(s) == d:
        return -1
    return s[d]
