# not stable quicksort for strings
# complexity 1.39*N*logN

def way_3_string_qs(a: [str]):
    sort(a, 0, len(a) - 1, 0)


def sort(a, lo, hi, d):
    if lo >= hi:
        return

    lt = lo
    gt = hi
    v = char_at(a[lo], d)
    i = lo + 1
    while i <= gt:
        t = char_at(a[i], d)
        if t < v:
            swap(a, lt, i)
            lt += 1
            i += 1
        elif t > v:
            swap(a, i, gt)
            gt -= 1
        else:
            i += 1

    # a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi]
    sort(a, lo, lt - 1, d)
    if v >= 0:
        sort(a, lt, gt, d + 1)
    sort(a, gt + 1, hi, d)


def char_at(s, d):
    if len(s) == d:
        return -1
    return ord(s[d])


def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t
