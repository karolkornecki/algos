from graphs.digraph import Digraph


# nondeterministic finite state automaton
# complexity: worst case O(M*N)
class NFA:
    def __init__(self, regexp):
        self.re = regexp
        self.m = len(regexp)  # number of states
        self.G = self._build_epsilon_transition_digraph()

    def _build_epsilon_transition_digraph(self):
        g = Digraph()

        # add vertices
        for v in range(self.m + 1):
            g.add_vertex(v)

        ops = []
        for i in range(self.m):
            lp = i
            if self.re[i] == '(' or self.re[i] == '|':
                ops.append(i)
            elif self.re[i] == ')':
                operator = ops.pop()
                if self.re[operator] == '|':
                    lp = ops.pop()
                    g.add_edge(lp, operator + 1)
                    g.add_edge(operator, i)
                elif self.re[operator] == '(':
                    lp = operator
                else:
                    raise Exception('invalid expression')
            if i < self.m - 1 and self.re[i + 1] == '*':
                g.add_edge(lp, i + 1)
                g.add_edge(i + 1, lp)

            if self.re[i] in ['(', '*', ')']:
                g.add_edge(i, i + 1)

        if len(ops) > 0:
            raise Exception('invalid expression')
        return g

    def recognizes(self, text):
        pc = set()  # set of possible states reachable from start by epsilon-transition
        d = dfs(self.G, [0])
        for v in self.G.vertices:
            if v in d:
                pc.add(v)

        for i in range(len(text)):  # states reachable after scanning past text[i] characters
            match = set()
            for v in pc:
                if v == self.m:
                    continue
                if self.re[v] == text[i] or self.re[v] == '.':
                    match.add(v + 1)

            if not match:
                continue

            d = dfs(self.G, match)  # follow epsilon-transition
            pc = set()
            for v in self.G.vertices:
                if v in d:
                    pc.add(v)

        # accept if can end in "m" state
        for v in pc:
            if v == self.m:
                return True
        return False


def dfs(g: Digraph, source: []) -> set:
    visited = set()
    for s in source:
        if s not in visited:
            visited.add(s)
            stack = [s]
            while stack:
                v = stack.pop()
                for w in g.adj(v):
                    if w not in visited:
                        visited.add(w)
                        stack.append(w)
    return visited

# What would you need to do in order to support the + closure operator (one or more repetitions)
# when constructing an NFA corresponding to a given regular expression?
# answer: Same as for the * closure operator but remove one ϵ-transition edge.
#
# Use the same construction as for the * closure operator (zero or more repetitions), except as follows:
# For a single-character closure, remove the edge from i to i + 1;
# for a parenthesized closure, remove the edge from lp to i+1
