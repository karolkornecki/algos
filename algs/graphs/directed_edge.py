class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def src(self):
        return self.v

    def dest(self):
        return self.w

    def __eq__(self, other):
        return self.v == other.v \
               and self.w == other.w \
               and self.weight == other.weight

    def __hash__(self):
        return hash((self.v, self.w, self.weight))

    def __cmp__(self, other):
        if self.weight < other.weight:
            return -1
        if self.weight > other.weight:
            return 1
        return 0

    def __le__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return f'{self.v}->{self.w}[{self.weight}]'
