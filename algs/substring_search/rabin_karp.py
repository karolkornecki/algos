# monte carlo version run linear time but can return false positive
# las vegas version guarantee to return correct result but in the worst case maybe m*n complexity
R = 256
# some long random prime
Q = 6728786102161


def rabin_karp(text, pattern):
    m = len(pattern)
    rm = 1
    i = 1
    while i <= m - 1:
        rm = (R * rm) % Q
        i += 1
    pattern_hash = _hash(pattern, m)

    # search
    n = len(text)
    if n < m:
        return -1

    text_hash = _hash(text, m)

    if text_hash == pattern_hash and check(text, pattern, 0):
        return 0

    i = m
    while i < n:
        text_hash = (text_hash + Q - rm * ord(text[i - m]) % Q) % Q
        text_hash = (text_hash * R + ord(text[i])) % Q
        offset = i - m + 1
        if text_hash == pattern_hash and check(text, pattern, offset):  # match
            return offset
        i += 1

    return -1  # not found


def _hash(key, m):
    """ Hash of the key"""
    h = 0
    for j in range(m):
        h = (R * h + ord(key[j])) % Q
    return h


# Las Vegas check
def check(text, pattern, i):
    for j in range(len(pattern)):
        if pattern[j] != text[i + j]:
            return False
    return True

# # Monte Carlo check
# def check(text, pattern, i):
#     return True
