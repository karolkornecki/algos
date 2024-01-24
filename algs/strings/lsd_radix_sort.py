R = 256  # extend ASCII alphabet size


# stable string sorting algorithm of fixed length
# complexity: linear

def lsd_sort(a: [str], w):
    """ 'w' -> number of characters in string """
    n = len(a)
    aux = [None for _ in range(n)]
    d = w - 1
    # sort by key-indexed counting on dth character
    while d >= 0:
        # compute frequency counts
        count = [0 for _ in range(R + 1)]
        for i in range(n):
            count[ord(a[i][d]) + 1] += 1

        # compute cumulates
        for r in range(R):
            count[r + 1] += count[r]

        # move data
        for i in range(n):
            aux[count[ord(a[i][d])]] = a[i]
            count[ord(a[i][d])] += 1

        # copy data
        for i in range(n):
            a[i] = aux[i]
        d -= 1
