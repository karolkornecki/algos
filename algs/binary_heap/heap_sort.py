# NlogN complexity guarantee but NOT stable
def heap_sort(a):
    if a is None or len(a) <= 1:
        return a
    n = len(a)

    # heapify
    for k in range(n // 2, 0, -1):
        sink(a, k, n)

    # sort phase
    k = n
    while k > 1:
        swap(a, 1, k)
        k -= 1
        sink(a, 1, k)


def swap(a, i, j):
    t = a[i - 1]
    a[i - 1] = a[j - 1]
    a[j - 1] = t


def sink(a, k, n):
    while 2 * k <= n:
        j = 2 * k
        if j < n and a[j - 1] < a[j]:
            j += 1
        if a[k - 1] >= a[j - 1]:
            break
        swap(a, k, j)
        k = j
