class Interval:
    def __init__(self, minimum: int, maximum: int):
        assert minimum < maximum
        self.min = minimum
        self.max = maximum

    def length(self):
        return self.max - self.min

    def intersect(self, other):
        return max(self.min, other.min) < min(self.max, other.max)

    def has(self, value):
        return self.min <= value <= self.max

    def contains(self, other):
        return self.min <= other.min and self.max >= other.max

    def merge(self, other):
        assert self.intersect(other)
        return Interval(min(self.min, other.min), max(self.max, other.max))
