from sort import knuth_shuffle as ks


# quick sort is NOT stable
def quick_sort(a):
    if a is None or len(a) <= 1:
        return a
    ks.shuffle(a)  # to prevent quadratic complexity
    qs(a, 0, len(a) - 1)


def qs(a, lo, hi):
    if lo > hi:
        return
    i = partition(a, lo, hi)
    qs(a, lo, i - 1)
    qs(a, i + 1, hi)


def partition(a, lo, hi):
    """
    partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi]
    :param a: array to partition
    :param lo: starting point
    :param hi: ending point
    :return: partitioning index
    """
    if a is None or len(a) <= 1:
        return a
    if lo > hi:
        raise Exception('invalid arguments')
    # select some pivot
    pivot = a[lo]
    start = lo + 1
    end = hi
    # now we need to move all elements less than pivot to the left
    # and all the grater elements to the right side of the array
    while True:
        while start <= end and a[start] < pivot:
            start += 1
        while start <= end and a[end] > pivot:
            end -= 1
        if start >= end:
            break
        swap(a, start, end)
    # swap pivot (lo) with end index
    swap(a, lo, end)
    return end


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
