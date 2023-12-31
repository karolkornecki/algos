# linear time shuffling
import random


def shuffle(a):
    for i in range(len(a)):
        r = random.randint(0, len(a) - 1)
        swap(a, i, r)


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


if __name__ == '__main__':
    array = [6, 5, 4, 3, 2, 1]
    print(array)
    for _ in range(10):
        shuffle(array)
        print(array)
