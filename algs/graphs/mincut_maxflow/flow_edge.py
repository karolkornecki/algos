class FlowEdge:
    def __init__(self, src, dest, capacity):
        self.src = src
        self.dest = dest
        self.capacity = capacity
        self.flow = 0

    def other(self, v):
        if self.src == v:
            return self.dest
        return self.src

    def residual_capacity_to(self, v):
        if v == self.src:
            return self.flow
        elif v == self.dest:
            return self.capacity - self.flow
        else:
            raise Exception(f'Invalid vertex <{v}>')

    def add_residual_flow_to(self, v, delta):
        if v == self.src:
            self.flow -= delta
        elif v == self.dest:
            self.flow += delta
        else:
            raise Exception(f'Invalid vertex <{v}>')

    def __eq__(self, other):
        return self.src == other.src \
               and self.dest == other.dest \
               and self.capacity == other.capacity

    def __hash__(self):
        return hash((self.src, self.dest, self.capacity))
