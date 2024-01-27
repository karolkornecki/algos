# need to precompute DFA (Deterministic finite state automaton) eg.: pattern ABABAC
# first state transition for each letter in the pattern
# \ A B A B A C
# A 1   3   5
# B   2   4
# C           6
# then if the mismatch occur we need to verify the longest prefix of pattern that is also suffix of text
# complexity O(m+n) instead of O(m*n) compared to brute-force
# hint: improved version of KMP uses NFA instead of DFA
R = 256  # extended ASCII


def kmp(text, pattern):
    # build dfa
    m = len(pattern)
    dfa = [[0 for _ in range(m)] for _ in range(R)]
    dfa[ord(pattern[0])][0] = 1
    x = 0
    j = 1
    while j < m:
        c = 0
        while c < R:
            dfa[c][j] = dfa[c][x]  # copy mismatch cases
            c += 1
        dfa[ord(pattern[j])][j] = j + 1  # set match case
        x = dfa[ord(pattern[j])][x]  # update restart state
        j += 1

    # search for pattern in text
    i = 0
    j = 0
    n = len(text)
    while i < n and j < m:
        j = dfa[ord(text[i])][j]
        i += 1

    if j == m:
        return i - m  # index of pattern occurrence
    # return n
    return -1  # not found
