from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def show_graph(self):
        for vertex, list in self.adjacency_list.items():
            print(f'{vertex} -> {list}')


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_edge(1,3)
my_graph.add_edge(2,4)
my_graph.add_edge(1,2)



if __name__ == '__main__':
    my_graph.show_graph()