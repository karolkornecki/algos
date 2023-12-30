def selection_sort(a):
    for i in range(len(a)):
        current_min = i
        for j in range(i, len(a)):
            if a[j] < a[current_min]:
                current_min = j
        swap(a, current_min, i)


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


if __name__ == '__main__':
    array = [6, 5, 4, 3, 2, 1]
    print(array)
    selection_sort(array)
    print(array)
