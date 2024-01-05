def binary_search(array, key):
    """
    Search for key value in sorted array
    :param array: sorted array
    :param key: search value
    :return: location index of key
    """

    def bs(a, k, lo, hi):
        if lo > hi:
            return None
        mid = lo + (hi - lo) // 2
        if a[mid] > k:
            return bs(a, k, lo, mid - 1)
        elif a[mid] < k:
            return bs(a, k, mid + 1, hi)
        else:
            return mid

    if array is None or len(array) == 0:
        return None
    return bs(array, key, 0, len(array) - 1)


def binary_search_iter(a, key):
    if a is None or len(a) == 0:
        return None
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] > key:
            hi = mid - 1
        elif a[mid] < key:
            lo = mid + 1
        else:
            return mid
