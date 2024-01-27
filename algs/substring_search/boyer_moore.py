# complexity in typical situation N/M but in wort case N*M, usually solved by adding KMP as a guard
R = 256  # extended ASCII


def boyer_moore(text, pattern):
    right = [1 for _ in range(R)]
    # rightmost occurrence of character in the pattern
    for i in range(len(pattern)):
        right[ord(pattern[i])] = i

    # search
    m = len(pattern)
    n = len(text)
    i = 0
    while i <= n - m:
        skip = 0
        j = m - 1
        while j >= 0:
            if pattern[j] != text[i + j]:
                skip = max(1, j - right[ord(text[i + j])])
                break
            j -= 1

        if skip == 0:
            return i  # found

        i += skip

    return -1  # not found
