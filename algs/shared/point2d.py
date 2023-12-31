class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def compare_by_y(point1, point2):
        """
        Description:
        ------------
        Compare two points by y coordinate, breaks tie by comparing x coordinate
        -----------
        Arguments:
        -----------
        :param point1: first point to compare
        :param point2: second point to compare
        :return: 1 if point1 is greater than point2, -1 if point2 is greater than point 1, 0 if they are equal
        """
        if point1.y < point2.y:
            return -1
        if point1.y > point2.y:
            return 1
        if point1.x < point2.x:
            return -1
        if point1.x > point2.x:
            return 1
        return 0

    @staticmethod
    def ccw(a, b, c):
        """
        Use determinant formula to calculate twice the area (signed) of a triangle and return if turn a->b->c is clockwise,
        counterclockwise, collinear:
        | ax ay 1 |
        | bx by 1 |
        | cx cy 1 |

        :param a: point
        :param b: point
        :param c: point
        :return: -1 clockwise, 0 collinear (in line), +1 counterclockwise if a -> b -> c turn
        """
        area = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        if area < 0:
            return -1
        elif area > 0:
            return +1
        else:
            return 0

    def compare_by_polar_angle(self, q1, q2):
        """
        Compare other points relative to polar angle (between 0 and 2pi) they make with this Point
        :param q1:
        :param q2:
        :return:
        """
        dx1 = q1.x - self.x
        dy1 = q1.y - self.y
        dx2 = q2.x - self.x
        dy2 = q2.y - self.y
        if dy1 >= 0 and dy2 < 0:
            return -1
        elif dy2 >= 0 and dy1 < 0:
            return 1
        elif dy1 == 0 and dy2 == 0:
            if dx1 >= 0 and dx2 < 0:
                return -1
            elif dx2 >= 0 and dx1 < 0:
                return 1
            else:
                return 0
        else:
            return -Point2D.ccw(self, q1, q2)

    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == '__main__':
    help(Point2D.compare_by_y)
