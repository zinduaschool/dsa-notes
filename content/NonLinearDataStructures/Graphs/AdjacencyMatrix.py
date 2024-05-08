class Graph:
    def __init__(self, no_of_vertices):
        self.no_of_vertices = no_of_vertices
        self.adjacency_matrix = [[0] * no_of_vertices for _ in range(no_of_vertices)]
        self.vertex_data = [''] * no_of_vertices

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_matrix[vertex1][vertex2] = weight
        self.adjacency_matrix[vertex2][vertex1] = weight

    def add_Vertext_data(self, vertex, data):
        self.vertex_data[vertex] = data

    def show_graph(self):
        print(f'X  {self.vertex_data}')
        for i in range(self.no_of_vertices):
            print(f'{self.vertex_data[i]} {self.adjacency_matrix[i]}')

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data) # find the index of the starting point
        distances = [float('inf')] * self.no_of_vertices # create the distance with the no of vertices
        distances[start_vertex] = 0 #set the distance of the starting point to be zero
        visited = [False] * self.no_of_vertices #tracking list checking if a vertice is visited or not

        for _ in range(self.no_of_vertices):
            min_distance = float('inf') #this the min distance to inf
            u = None # track the current node 
            for i in range(self.no_of_vertices):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.no_of_vertices):
                if self.adjacency_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adjacency_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        print(distances)


my_graph = Graph(5)
my_graph.add_edge(0,1, 4)
my_graph.add_edge(2,3, 5)
my_graph.add_edge(1,4, 6)
my_graph.add_Vertext_data(0, 10)
my_graph.add_Vertext_data(1, 20)
my_graph.add_Vertext_data(2, 30)
my_graph.add_Vertext_data(3, 40)
my_graph.add_Vertext_data(4, 50)
my_graph.dijkstra(40)
my_graph.show_graph()
