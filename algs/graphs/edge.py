class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, v=None):
        if self.v == v:
            return self.w
        return self.v

    def __eq__(self, other):
        return self.v == other.v \
               and self.w == other.w \
               and self.weight == other.weight

    def __hash__(self):
        return hash((self.v, self.w, self.weight))
