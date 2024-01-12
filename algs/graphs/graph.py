class Graph:
    """
    Graph abstraction
    """

    def v(self) -> int:
        """
        Return number of vertices
        """
        pass

    def e(self) -> int:
        """
        Return number of edges
        """
        pass

    def adj(self, v) -> [int]:
        """
        Return edges from vertex v
        """
        pass

    def add_edge(self, v: int, w: int) -> None:
        """
        Add edge between v and w
        """
        pass