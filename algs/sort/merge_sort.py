# merge sort is stable (insertion sort as well) - preserve ordering of items with equal keys
def merge_sort(a):
    if a is None or len(a) == 0 or len(a) == 1:
        return a
    aux = [0 for _ in range(len(a))]
    sort(a, aux, 0, len(a) - 1)


# iterative (bottom-up) version
def merge_sort_bu(a):
    if a is None or len(a) == 0 or len(a) == 1:
        return a
    n = len(a)
    aux = [0 for _ in range(n)]
    length = 1
    while length < n:
        lo = 0
        while lo < n - length:
            mid = lo + length - 1
            hi = min(lo + length + length - 1, n - 1)
            merge(a, aux, lo, mid, hi)
            lo += (length + length)
        length *= 2


def sort(a, aux, start, end):
    if start >= end:
        return
    mid = start + (end - start) // 2
    sort(a, aux, start, mid)
    sort(a, aux, mid + 1, end)
    merge(a, aux, start, mid, end)


def merge(a, aux, start, mid, end):
    # copy to aux[]
    for i in range(start, end + 1):
        aux[i] = a[i]

    i = start
    j = mid + 1

    # then back assign to a[]
    for k in range(start, end + 1):
        if i > mid:  # i is out of range
            a[k] = aux[j]
            j += 1
        elif j > end:  # j is out of range
            a[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            a[k] = aux[i]
            i += 1
        else:
            a[k] = aux[j]
            j += 1


if __name__ == '__main__':
    array_1 = [7, 6, 5, 4, 3, 2, 1]
    print(array_1)
    merge_sort(array_1)
    print(array_1)
    array_2 = [7, 6, 5, 4, 3, 2, 1]
    print(array_2)
    merge_sort(array_2)
    print(array_2)
