# PREMIUM
from typing import List


# Runtime
# 398ms Beats 26.56% of users with Python3
# Memory
# 17.14MB Beats 72.66% of users with Python3
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        min_x, max_x = x, x
        min_y, max_y = y, y
        pq = [(x, y)]
        image[x][y] = '0'  # mark visited
        while pq:
            (cx, cy) = pq.pop(0)
            min_x = min(min_x, cx)
            max_x = max(max_x, cx)
            min_y = min(min_y, cy)
            max_y = max(max_y, cy)
            for nx, ny in neighbours(image, cx, cy):
                pq.append((nx, ny))
                image[nx][ny] = '0'
        return (max_y - min_y + 1) * (max_x - min_x + 1)


def neighbours(image, x, y):
    n = []
    if x - 1 >= 0 and image[x - 1][y] == '1':
        n.append((x - 1, y))
    if x + 1 < len(image) and image[x + 1][y] == '1':
        n.append((x + 1, y))
    if y - 1 >= 0 and image[x][y - 1] == '1':
        n.append((x, y - 1))
    if y + 1 < len(image[0]) and image[x][y + 1] == '1':
        n.append((x, y + 1))
    return n
