from sort import knuth_shuffle as ks
from sort import quick_sort as qs


# Hoare's quick select algorithm
# O(n) complexity to find kth-smallest element in the array
def quick_select(a, k):
    if a is None or k >= len(a):
        raise Exception('invalid arguments')
    ks.shuffle(a)
    start = 0
    end = len(a) - 1
    while start <= end:
        pivot = qs.partition(a, start, end)
        if pivot > k:
            end -= 1
        elif pivot < k:
            start += 1
        else:
            return a[k]
