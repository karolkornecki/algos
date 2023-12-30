def shell_sort(a):
    n = len(a)
    h = 1
    while h < n // 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and a[j] < a[j - h]:
                swap(a, j, j - h)
                j -= h
        h //= 3


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


if __name__ == '__main__':
    array = [7, 6, 5, 4, 3, 2, 1]
    print(array)
    shell_sort(array)
    print(array)
