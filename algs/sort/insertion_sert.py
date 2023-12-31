def insertion_sort(a):
    for i in range(len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                swap(a, j, j - 1)


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


if __name__ == '__main__':
    array = [6, 5, 4, 3, 2, 1]
    print(array)
    insertion_sort(array)
    print(array)
