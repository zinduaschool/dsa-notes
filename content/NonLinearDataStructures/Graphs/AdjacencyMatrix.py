class Graph:
    def __init__(self, no_of_vertices):
        self.no_of_vertices = no_of_vertices
        self.adjacency_matrix = [[0] * no_of_vertices for _ in range(no_of_vertices)]

    def add_edge(self, vertex1, vertex2):
        self.adjacency_matrix[vertex1][vertex2] = 1
        self.adjacency_matrix[vertex2][vertex1] = 1

    def show_graph(self):
        for row in self.adjacency_matrix:
            print(row)


my_graph = Graph(5)
my_graph.add_edge(0,1)
my_graph.add_edge(2,3)
my_graph.add_edge(1,4)
my_graph.show_graph()
