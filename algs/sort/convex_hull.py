from functools import cmp_to_key
from typing import List

import matplotlib.pyplot as plt

from shared.point2d import Point2D


# compute the convex hull using Graham scan algorithm.
def graham_scan(points: List[Point2D]):
    if points is None or len(points) == 0:
        return
    n = len(points)
    # defensive copy array
    a = [p for p in points]

    # sort by y coordinate a[0] has lowest y-coordinate
    # a[0] is an extreme point of the convex hull
    sorted(a, key=cmp_to_key(Point2D.compare_by_y))

    # sort a[1,...,n] by its polar angle base on a[0]
    a = [a[0], *sorted(a[1::], key=cmp_to_key(a[0].compare_by_polar_angle))]

    # first point in hull
    hull = [a[0]]

    # find first point != a[0]
    a1 = 1
    for i in range(a1, n):
        if a[0] != a[i]:
            a1 = i
            break
    # all point are equal
    if a1 == n:
        return

    # find first point not collinear with a0 and a1
    a2 = a1 + 1
    for i in range(a1, n):
        if Point2D.ccw(a[0], a[a1], a[i]) != 0:
            a2 = i
            break
    hull.append(a[a2 - 1])  # second extreme point

    # Graham scan, a[n-1] is extreme point different from a[0]
    for i in range(a2, n):
        top = hull.pop()
        while Point2D.ccw(hull[-1], top, a[i]) <= 0:
            top = hull.pop()
        hull.append(top)
        hull.append(a[i])

    # assert in_convex()
    return hull, a  # 'a' array is return just for plotting


def draw_initial_points(points):
    ax = plt.subplot()
    color = 'red'
    for i in range(len(points)):
        if i > 0:
            color = 'blue'
        ax.plot(points[i].x, points[i].y, '.', color=color)
        ax.annotate(f' [{i}]', (points[i].x, points[i].y), color=color)


def draw_convex_hull_points(points):
    ax = plt.subplot()
    color = 'red'
    for i in range(len(points)):
        ax.plot(points[i].x, points[i].y, '.', color=color)
        ax.annotate(f'        [{i}]', (points[i].x, points[i].y), color=color)


if __name__ == '__main__':
    pts = [
        (7486.0, 422.0),
        (29413.0, 596.0),
        (32011.0, 3140.0),
        (30875.0, 28560.0),
        (28462.0, 32343.0),
        (15731.0, 32661.0),
        (822.0, 32301.0),
        (823.0, 15895.0),
        (1444.0, 10362.0),
        (4718.0, 4451.0),
        (10400, 13000),
        (12400, 6500),
        (6000, 22000),
        (17000, 20000),
        (23000, 10000),
        (25000, 27000),
    ]
    points2d = [Point2D(x, y) for x, y in pts]
    hull, sorted_points = graham_scan(points2d)
    draw_initial_points(sorted_points)
    draw_convex_hull_points(hull)

    plt.show()
